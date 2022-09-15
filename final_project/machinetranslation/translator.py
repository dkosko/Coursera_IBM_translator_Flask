"""This module creates connection instance to IBM translator API
and use it for translation issues"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


def create_connection():
    """Function creates connection instance to IBM translator API"""
    # load apikey and url params from .env
    load_dotenv()
    apikey = os.environ['apikey']
    url = os.environ['url']

    # Connect to IBM language translator API
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator


def valid_translator_input(text_to_translate):
    """Function validates if input to translator func can be processed"""
    null_cases = (None, '', ' ')
    if text_to_translate in null_cases:
        return None
    else:
        return 1

def english_to_french(english_text):
    """Function translatest english statement into french
    input: englishText:str
    output: frenchText:str"""
    val_result = valid_translator_input(english_text)
    if not val_result == 1:
        return val_result

    language_translator = create_connection()
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """Function translatest french statement into english
        input: frenchText:str
        output: englishText:str"""
    val_result = valid_translator_input(french_text)
    if  not val_result == 1:
        return val_result

    language_translator = create_connection()
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text


if __name__ == "__main__":
    EN_TEXT = 'hello'
    FR_TEXT = 'bonjour'
    en_to_fr = english_to_french(EN_TEXT)
    fr_to_en = french_to_english(FR_TEXT)
    print(fr_to_en)
