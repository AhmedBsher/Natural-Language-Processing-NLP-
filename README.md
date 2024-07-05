# Natural-Language-Processing-NLP-
"This Python-based sentiment analysis tool integrates NLTK for sentiment analysis using VADER, SpaCy for entity recognition, and Plotly for visualization. It offers features like sentiment timeline analysis, word cloud generation for positive and negative sentiments, and entity filtering by types such as PERSON, ORG, GPE, and DATE."


# Sentiment Analysis Tool

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![NLTK](https://img.shields.io/badge/nltk-3.6.6-brightgreen)
![SpaCy](https://img.shields.io/badge/spacy-3.2.1-yellow)
![Plotly](https://img.shields.io/badge/plotly-5.3.1-orange)
![WordCloud](https://img.shields.io/badge/wordcloud-1.8.1-red)

This is a sentiment analysis tool built in Python using NLTK for sentiment analysis with VADER, SpaCy for entity recognition, and Plotly for visualization. It provides features like sentiment timeline analysis, word cloud generation for positive and negative sentiments, and entity filtering based on types like PERSON, ORG, GPE, and DATE.


## Features

- **Sentiment Analysis:** Analyze sentiment of input text using NLTK's VADER sentiment analyzer.
- **Entity Recognition:** Utilize SpaCy's pre-trained model for named entity recognition (NER) in the input text.
- **Visualization:** Visualize sentiment timeline and generate word clouds for positive and negative sentiment categories.
- **Entity Filtering:** Filter entities by type (PERSON, ORG, GPE, DATE) for targeted sentiment analysis.


## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/sentiment-analysis-tool.git.
cd sentiment-analysis-tool
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate # For Windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the application:
```
python sentiment_analysis_tool.py
```

2. Enter or paste text into the GUI window to analyze sentiment. Optionally, filter entities by selecting a type from the dropdown menu.

3. Click "Analyze Sentiment" to see the sentiment timeline and word clouds for positive and negative sentiments.


## Dependencies

- Python 3.7 or higher
- NLTK 3.6.6
- SpaCy 3.2.1
- Plotly 5.3.1
- WordCloud 1.8.1


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
