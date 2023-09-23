from gensim.models.phrases import Phrases
from gensim.models import FastText
import pandas as pd

# Load the data
df = pd.read_csv('insert_path_here')  # Replace 'insert_path_here' with the path to your CSV file

# Convert the desired column to a list
documents = df['column_name'].to_list()  # Replace 'column_name' with the name of the column you want to use

# Split each document into words
sentence_stream = [doc.split(" ") for doc in documents]

# Construct bigram model
bigram = Phrases(sentence_stream, min_count=1, threshold=2, delimiter=b' ')

# This line can be used to further create a trigram model
# trigram = Phrases(bigram[sentence_stream], min_count=1, delimiter=b' ')

# Train a FastText model on the bigrams
model = FastText([bigram[sent] for sent in sentence_stream], min_count=1)
