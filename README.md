# MathGen

**MathGen** est un projet open-source visant à générer des questions de mathématiques pour le niveau lycée, accompagnées de leurs solutions détaillées. Ce projet est conçu pour aider les étudiants à s'entraîner, les enseignants à créer des supports pédagogiques, et les développeurs à explorer des applications d'intelligence artificielle dans le domaine éducatif.

## Fonctionnalités principales

- **Génération de questions de mathématiques** : Questions variées couvrant des thématiques telles que l'algèbre, la géométrie, l'analyse, et les probabilités.
- **Solutions détaillées** : Chaque question est accompagnée d'une solution complète.
- **Personnalisation** : Possibilité d'adapter le niveau de difficulté et les types de questions générées.
- **API facile à intégrer** : Fournir un accès programmatique pour inclure MathGen dans d'autres outils.

## Structure du projet

```
MathGen/
├── data/                # Datasets de questions et réponses générées
├── models/              # Scripts et modèles pour la génération de questions
├── examples/            # Exemples d'utilisation du projet
├── tests/               # Tests pour valider le fonctionnement des modules
├── scripts/             # Scripts utilitaires pour la gestion et la génération de données
├── README.md            # Description du projet
├── LICENSE              # Licence du projet
└── CONTRIBUTING.md      # Guide pour contribuer au projet
```

## Installation

1. Clonez le repository :

```bash
git clone https://github.com/votre-utilisateur/mathgen.git
```

2. Accédez au répertoire :

```bash
cd mathgen
```

3. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Pour générer des questions de mathématiques :

```bash
python scripts/generate_questions.py --topic algebra --difficulty medium
```

Exemple de résultat :

```
Question : Résolvez l'équation 2x + 3 = 7.
Réponse : x = 2.
```

## Contribution

Les contributions sont les bienvenues ! Veuillez consulter le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour des instructions détaillées sur la manière de contribuer.

## Feuille de route

- [ ] Générer des questions de base en algèbre.
- [ ] Ajouter des questions de géométrie.
- [ ] Implémenter une interface utilisateur web.
- [ ] Fournir une API REST.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

Pour toute question ou suggestion, ouvrez une issue ou contactez-nous à **votre-email@example.com**.

---
