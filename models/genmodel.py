from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
import torch
import json
import os

# Charger le dataset
dataset_path = os.path.join("data", "dataset.json")  # Assurez-vous que ce fichier est dans le dossier 'data'
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Le fichier {dataset_path} est introuvable.")
    
with open(dataset_path, "r", encoding="utf-8") as f:
    dataset = json.load(f)
print(f"Dataset chargé : {len(dataset)} entrées")

# Préparer les données pour l'entraînement
def prepare_data(dataset):
    inputs = []
    outputs = []
    for entry in dataset:
        topic = entry["Topic"]
        question = entry["Question"]
        answer = entry.get("Answer", "")
        inputs.append(f"Create a math problem for the topic {topic}, labeled as 'Question:' and provide its solution labeled as 'Answer:'.")
        outputs.append(f"Question: {question} Answer: {answer}")
    return inputs, outputs

inputs, outputs = prepare_data(dataset)

# Vérification des données
print(f"Exemple d'entrée : {inputs[0]}")
print(f"Exemple de sortie : {outputs[0]}")

# Diviser en ensembles d'entraînement et de validation
train_inputs, val_inputs, train_outputs, val_outputs = train_test_split(inputs, outputs, test_size=0.2, random_state=42)

# Charger le tokenizer et le modèle T5
model_name = "t5-base"  # Changez à "google/flan-t5-base" pour de meilleures performances
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Encodage des données
def tokenize_data(inputs, outputs, tokenizer, max_length=512):
    encodings = tokenizer(inputs, padding=True, truncation=True, max_length=max_length, return_tensors="pt")
    targets = tokenizer(outputs, padding=True, truncation=True, max_length=max_length, return_tensors="pt")
    return encodings, targets

train_encodings, train_targets = tokenize_data(train_inputs, train_outputs, tokenizer)
val_encodings, val_targets = tokenize_data(val_inputs, val_outputs, tokenizer)

# Convertir en Dataset PyTorch
class MathDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, targets):
        self.encodings = encodings
        self.targets = targets

    def __len__(self):
        return len(self.encodings["input_ids"])

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item["labels"] = self.targets["input_ids"][idx]
        return item

train_dataset = MathDataset(train_encodings, train_targets)
val_dataset = MathDataset(val_encodings, val_targets)

# Configuration de l'entraînement
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=10,  # Augmentez les époques pour une meilleure convergence
    per_device_train_batch_size=4,  # Réduisez si vous avez des limitations mémoire
    per_device_eval_batch_size=4,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=3e-5,  # Un taux d'apprentissage plus stable
    load_best_model_at_end=True,
)

# Initialisation de l'entraîneur
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
)

# Entraîner le modèle
print("Début de l'entraînement...")
trainer.train()
print("Entraînement terminé.")

# Sauvegarder le modèle
output_dir = "./mathgen_model"
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
print(f"Modèle sauvegardé dans le répertoire : {output_dir}")

# Fonction pour générer une question
def generate_question(topic, model, tokenizer, max_length=100):
    input_text = f"Create a math problem for the topic {topic}, labeled as 'Question:' and provide its solution labeled as 'Answer:'."
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True).to(model.device)
    outputs = model.generate(inputs["input_ids"], max_length=max_length, num_beams=5, early_stopping=True)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Prompt : {input_text}")
    print(f"Generated Output : {decoded}")
    return decoded

# Exemple d'utilisation
model.eval()
topic = "Algebra"
generated_output = generate_question(topic, model, tokenizer)
print(f"Generated Question:\n{generated_output}")
