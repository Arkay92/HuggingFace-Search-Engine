# HuggingFace-Search-Engine

A simple, lightweight search engine designed to facilitate keyword-based search with relevance scoring across textual datasets hosted on Hugging Face.

## Features
- Keyword search on any textual dataset available on Hugging Face.
- Relevance scoring based on the frequency of query terms.
- Easy-to-use command-line interface.

## Installation

First, clone this repository:

```bash
git clone https://github.com/Arkay92/HuggingFace-Search-Engine.git
```

## Navigate into the cloned directory:

```
cd HuggingFace-Search-Engine
```

## Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage
To use the search engine, run the script with the dataset name and your search query:

```
python search_engine.py <dataset-name> "your search query"
```

Replace <dataset-name> with the name of the dataset you wish to search, and "your search query" with your actual query.

### Example
```
python search_engine.py teknium/GPT4-LLM-Cleaned "artificial intelligence"
```

This command will search for the term "artificial intelligence" within the GPT-4 LLM Cleaned dataset on Hugging Face.

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## License
This project is open-source and available under the MIT License.
