from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm
import json
from accelerate import infer_auto_device_map, init_empty_weights
import torch

# Charger le modèle et le tokenizer
model_name = "google/flan-t5-xl"  # Modèle très précis
print("Chargement du modèle...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

def load_model_with_accelerate(model_name):
    """Charge le modèle avec accelerate pour optimiser l'utilisation des ressources"""
    device_map = infer_auto_device_map(AutoModelForSeq2SeqLM.from_pretrained(model_name), max_memory={0: "6GiB", "cpu": "12GiB"})
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, device_map=device_map)
    return model

model = load_model_with_accelerate(model_name)

# Fonction pour générer des questions et réponses
def generate_question_and_answer(prompt, max_length=150):
    print(f"Prompt utilisé: {prompt}")
    inputs = tokenizer(prompt, return_tensors="pt", max_length=128, truncation=True)
    inputs = {k: v.to(next(model.parameters()).device) for k, v in inputs.items()}
    outputs = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        num_return_sequences=3,  # Générer plusieurs réponses pour augmenter les chances de cohérence
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    print(f"Réponses générées: {responses}")
    return responses

# Liste des sujets et prompts (prompts améliorés)
subjects = ["Algebra", "Geometry", "Probability", "Statistics"]
prompts = {
    "Algebra": "Generate a clear math problem labeled 'Question:' about solving for x in a linear equation and provide its answer labeled 'Answer:'.",
    "Geometry": "Generate a clear geometry problem labeled 'Question:' about calculating the area of a shape and provide its answer labeled 'Answer:'.",
    "Probability": "Generate a clear probability problem labeled 'Question:' about rolling dice and provide its answer labeled 'Answer:'.",
    "Statistics": "Generate a clear statistics problem labeled 'Question:' about finding the average of numbers and provide its answer labeled 'Answer:'."
}

# Générer un dataset
print("Génération du dataset...")
dataset = []

for subject in tqdm(subjects, desc="Sujets"):
    for _ in tqdm(range(5), desc=f"Questions pour {subject}", leave=False):  # Ajusté à 5 pour tester plus rapidement
        prompt = prompts[subject]
        outputs = generate_question_and_answer(prompt)
        for output in outputs:
            parts = output.split("Answer:")
            if len(parts) == 2:
                question = parts[0].replace("Question:", "").strip()
                answer = parts[1].strip()
                print(f"Question extraite: {question}")
                print(f"Réponse extraite: {answer}")
                dataset.append({"Topic": subject, "Question": question, "Answer": answer})
                break  # Utilise la première réponse valide trouvée

# Sauvegarder le dataset dans un fichier JSON
output_file = "generated_math_questions_with_answers.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)

print(f"Dataset sauvegardé dans le fichier : {output_file}")
