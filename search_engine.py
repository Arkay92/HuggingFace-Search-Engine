from datasets import load_dataset
import pandas as pd
import argparse
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Attempt to download NLTK stopwords and tokenizer data
try:
    nltk.download('punkt')
    nltk.download('stopwords')
except Exception as e:
    print(f"Error downloading nltk data: {e}")
    exit(1)

class SimpleSearchEngine:
    def __init__(self, dataset_name):
        try:
            # Load the dataset from Hugging Face
            self.dataset = load_dataset(dataset_name, split='train')
        except Exception as e:
            print(f"Failed to load dataset: {e}")
            exit(1)
        
        # Convert the dataset to a Pandas DataFrame for easier manipulation
        if 'text' in self.dataset.column_names:
            self.dataset_df = pd.DataFrame(self.dataset)
            self.inverted_index = self._build_inverted_index()
        else:
            print("Dataset does not contain a 'text' column.")
            exit(1)

    def _build_inverted_index(self):
        inverted_index = {}
        stop_words = set(stopwords.words('english'))

        for index, row in self.dataset_df.iterrows():
            words = word_tokenize(row['text'].lower())
            filtered_words = [word for word in words if word not in stop_words and word.isalpha()]

            for word in filtered_words:
                if word in inverted_index:
                    if index not in inverted_index[word]:
                        inverted_index[word].append(index)
                else:
                    inverted_index[word] = [index]

        return inverted_index

    def search(self, query):
        words = word_tokenize(query.lower())
        results = {}
        for word in words:
            if word in self.inverted_index:
                for doc_index in self.inverted_index[word]:
                    if doc_index in results:
                        results[doc_index] += 1
                    else:
                        results[doc_index] = 1

        # Sort results by relevance
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
        return self.dataset_df.iloc[[doc_index for doc_index, _ in sorted_results]]

def main():
    parser = argparse.ArgumentParser(description='Enhanced Search Engine for Hugging Face Datasets')
    parser.add_argument('dataset_name', type=str, help='Name of the Hugging Face dataset')
    parser.add_argument('query', type=str, help='Search query')

    args = parser.parse_args()

    try:
        search_engine = SimpleSearchEngine(args.dataset_name)
        results = search_engine.search(args.query)
        if results.empty:
            print("No results found.")
        else:
            print(results)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
