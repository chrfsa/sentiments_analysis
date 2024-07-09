# Analyse de Sentiments avec FastAPI et Transformers

## Description
Ce projet utilise FastAPI pour créer une API de classification de sentiments basée sur le modèle Transformers de Hugging Face. Un front-end est développé avec Streamlit pour interagir avec l'API.

## Table des Matières
1. [Installation](#installation)
2. [Usage](#usage)


## Installation

### Prérequis
- Python 3.6 ou supérieur

### Étapes
1. Clonez le dépôt :
    ```bash
    git clone https://github.com/chrfsa/sentiments_analysis.git
    cd sentiments_analysis
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    # Sous Windows
    .\venv\Scripts\activate
    # Sous macOS et Linux
    source venv/bin/activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Lancez le serveur FastAPI :
    ```bash
    # avec uvicorn
    uvicorn api:app --reload
    # avec fastapi
    fastapi dev api.py
    ```

5. Lancez l'application Streamlit :
    ```bash
    streamlit run app.py
    ```

## Usage
### API
L'API FastAPI expose un point de terminaison `/analyse` pour l'analyse des sentiments. Envoyez une requête POST avec un JSON contenant le texte à analyser :
```json
{
    "prompts": "votre texte ici"
}
