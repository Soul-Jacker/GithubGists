# GithubGists


## Scripts Included

1. **RIS to DataFrame Converter**
   - Reads `.ris` files and converts the bibliographic entries into a consolidated pandas DataFrame.
  
2. **Phrase Modeling with Gensim**
   - Utilizes Gensim's Phrases model to identify and create bigrams and potentially trigrams from a given text corpus.

3. **Spacy Language Detector**
   - Integrates `spacy` and `spacy_langdetect` to identify the language of each row in a DataFrame.
   
4. **Spacy Sentence Splitter**
   - Splits text in a DataFrame into sentences using Spacy's natural language processing capabilities.

5. **Named Entity Anonymizer**
   - Anonymizes named entities (people's names, dates, organizations, and places) in text data using `spacy`.

---

## Getting Started

### Dependencies

You will need to install the following Python packages if you haven't:

```bash
pip install spacy
pip install pandas
pip install numpy
pip install gensim
pip install spacy_langdetect
pip install RISparser
```

And also download the Spacy language model:

```bash
python -m spacy download en_core_web_sm
```

### How to Run Scripts

Replace the placeholder comments like `# Insert Path Here` with the actual file paths before running the scripts.

---

## Usage

Each script has specific usage patterns described within the script as comments. Here are general steps to follow:

1. **RIS to DataFrame Converter**
   - Make sure the `.ris` files are present in the script directory.
   - Run the script.

2. **Phrase Modeling with Gensim**
   - Replace the placeholder for DataFrame column and file path.
   - Run the script.

3. **Spacy Language Detector**
   - Replace the placeholder for DataFrame column and file path.
   - Run the script.

4. **Spacy Sentence Splitter**
   - Replace the placeholder for DataFrame column and file path.
   - Run the script.

5. **Named Entity Anonymizer**
   - Replace the placeholder for DataFrame column and file path.
   - Run the script.

---

## Note

While the anonymizer script performs a basic level of anonymization, please review the output carefully when dealing with sensitive or personally identifiable information to ensure adequate privacy protection.

---

## Contributing

Feel free to fork this repository and contribute. Pull requests are welcome.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## Contact

If you have any questions or need further clarification, feel free to contact the maintainers.
