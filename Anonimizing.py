import spacy
import pandas as pd
import numpy as np
import random

nlp = spacy.load("en_core_web_sm")

def get_unique_elements(list1):
    """Return unique elements from a list."""
    return np.unique(np.array(list1))

def anonymize(df, column, id_optional=None):
    """Anonymize a given column in a dataframe based on NER tags."""
    unique_names = set()
    unique_places = set()
    unique_dates = set()
    unique_orgs = set()
    
    result = []
    ids = 0
    
    for sentence in df[column]:
        doc = nlp(sentence)
        original = sentence
        
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                unique_names.add(ent.text)
            elif ent.label_ == 'ORG':
                unique_orgs.add(ent.text)
            elif ent.label_ == 'DATE':
                unique_dates.add(ent.text)
            elif ent.label_ == 'GPE':
                unique_places.add(ent.text)
        
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                sentence = sentence.replace(ent.text, random.choice(list(unique_names)))
            elif ent.label_ == 'ORG':
                sentence = sentence.replace(ent.text, random.choice(list(unique_orgs)))
            elif ent.label_ == 'DATE':
                sentence = sentence.replace(ent.text, random.choice(list(unique_dates)))
            elif ent.label_ == 'GPE':
                sentence = sentence.replace(ent.text, random.choice(list(unique_places)))
        
        result.append({
            'ID': ids,
            'Original_text': original,
            'Anonymous_Text': sentence
        })
        ids += 1
        
    return pd.DataFrame(result)

# Sample usage
# df = pd.read_excel('path_to_excel_file.xlsx')
# anonymized_df = anonymize(df, 'Sentence')
