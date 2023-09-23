# Ensure spacy_fastlang and spacy-transformers are installed before executing.
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
import pandas as pd

def get_lang_detector(nlp, name):
    return LanguageDetector()

nlp = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)

# Load the data
df = pd.read_csv('INSERT_PATH_HERE')  # Replace 'INSERT_PATH_HERE' with the path to your CSV file

# Detect language for each row in the DataFrame
def detect_language(text):
    doc = nlp(text)
    return pd.Series([doc._.language['language'], doc._.language['score']], index=['language', 'Score'])

df[['language', 'Score']] = df['Text'].apply(detect_language)

print(df)
