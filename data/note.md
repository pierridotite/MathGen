## Notes sur la génération des questions mathématiques

### Contexte
Lors de la tentative de génération de questions mathématiques et de leurs réponses associées en utilisant le modèle **Flan-T5-XL**, plusieurs problèmes ont été rencontrés. Malgré les ajustements des prompts et des paramètres de génération, les résultats n'étaient pas conformes aux attentes.

### Problèmes rencontrés
1. **Manque de précision dans les questions :**
   - Les questions générées étaient souvent vagues ou peu pertinentes pour le sujet visé.
   - Exemple : "What is the area of a rectangle?" sans données supplémentaires.

2. **Réponses absentes ou incorrectes :**
   - Dans plusieurs cas, aucune réponse valide n'était fournie par le modèle.
   - Certaines sorties étaient des phrases incohérentes ou hors sujet.

3. **Limitations matérielles :**
   - La mémoire disponible (même avec un GPU dans Google Colab) limitait les performances du modèle lors de générations prolongées.

### Décision
Pour surmonter ces limitations, j’ai décidé d'utiliser **ChatGPT (GPT-4)** pour générer les questions et les réponses mathématiques. Ce modèle présente les avantages suivants :
- **Précision et pertinence :** Les questions générées sont contextualisées et incluent des réponses claires.
- **Flexibilité :** Permet de générer rapidement des contenus personnalisés.

### Exemple de questions générées avec GPT
Voici quelques exemples de questions générées par GPT :

1. **Algebra**
   - Question : Solve for x in the equation 3x + 2 = 11.
   - Answer : x = 3.

2. **Geometry**
   - Question : Calculate the area of a circle with a radius of 7.
   - Answer : Area = 153.94 (using π ≈ 3.14).

3. **Probability**
   - Question : What is the probability of rolling a 4 on a fair 6-sided die?
   - Answer : The probability is 1/6.

4. **Statistics**
   - Question : Find the mean of the numbers 4, 8, 15, and 16.
   - Answer : Mean = 10.75.

### Conclusion
Bien que l’idée d'utiliser un modèle préentrané pour générer automatiquement un dataset soit prometteuse, les limitations pratiques et les résultats inattendus ont rendu cette approche impraticable dans ce contexte. GPT a été utilisé comme alternative pour fournir un dataset cohérent et de qualité.

Si vous avez des suggestions pour améliorer le processus ou des retours, n’hésitez pas à partager.