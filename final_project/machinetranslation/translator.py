"""
Just an Api for language translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    """
    This function lets translates from english to french
    """
    if englishText is None:
        return None
    resp_data = language_translator.translate(text=englishText, model_id="en-fr").get_result()
    frenchText = resp_data['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """
    This function lets translates from french to english
    """
    if frenchText is None:
        return None
    resp_data = language_translator.translate(text=frenchText, model_id="fr-en").get_result()
    englishText = resp_data['translations'][0]['translation']
    return englishText
