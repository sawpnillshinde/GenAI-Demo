import streamlit as st
import requests

# Streamlit app title and description
st.title('Language Translation App')
st.write('Select the target language to translate into:')

# Dropdown menu for selecting the target language
target_language = st.selectbox('Select Language', ['French', 'Spanish', 'German', 'Hindi', 'Korean'])

# Input text field for entering the text to be translated
input_text = st.text_area('Enter the text to translate', '')

# Button to trigger the translation
if st.button('Translate'):
    # API request to translate the text into the selected language
    translation_endpoint = f'http://127.0.0.1:8000/translate?language={target_language.lower()}&text={input_text}'
    response = requests.get(translation_endpoint)
    
    if response.status_code == 200:
        translated_text = response.json().get('translated_text', 'Translation Error')
        st.write(f'Translated Text ({target_language}): {translated_text}')
    else:
        st.write('Translation Error. Please try again.')