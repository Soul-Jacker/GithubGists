import spacy
import pandas as pd

# Load the Spacy Model
nlp = spacy.load('en_core_web_sm')

# Load the data
df = pd.read_excel('INSERT_PATH_HERE')  # Replace 'INSERT_PATH_HERE' with the path to your excel file.

def split_text_into_sentences(text, ID):
    doc = nlp(text)
    sentences = list(doc.sents)
    
    # List comprehension to generate the data for each sentence
    return [{'ID': ID, 'Position': idx+1, 'Text': str(sentence)} for idx, sentence in enumerate(sentences)]

# Applying the function to each row
result = df.apply(lambda row: split_text_into_sentences(row['Text'], row['ID']), axis=1)

# Flattening the result
result_list = [item for sublist in result for item in sublist]

# Convert the list of dictionaries to DataFrame
end = pd.DataFrame(result_list)

print(end)
