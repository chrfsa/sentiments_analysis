import requests
import streamlit as st

# URL of your FastAPI API
API_URL = 'http://localhost:8000'  # Update with your FastAPI URL

# Function to call the FastAPI API
def call_api(input_text):
    """call api is a fonction cal analyse api

    Args:
        input_text (string): like prompt

    Returns:
        feeling and probability: after the analysis of prompt the models return the feeling and the probability of this feeling
    """
    endpoint = f"{API_URL}/analyse"
    payload = {"prompts": input_text}
    response = requests.post(endpoint, json=payload)
    return response.json()

# frontend with strealkit
def main():
    st.title('Analyse de Sentiment avec Transformers et FastAPI')

    # Text box to enter the text to analyze
    prompts = st.text_area('Entrez le texte à analyser :')

    # Button to submit text to API
    if st.button('Analyser'):
        if prompts:
            # call api.
            result = call_api(prompts)
            st.write('Sentiment :', result[0]['label'])
            st.write('Confiance :', result[0]['score'])

if __name__ == '__main__':
    main()
