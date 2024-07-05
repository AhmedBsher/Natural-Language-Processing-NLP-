import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy
import plotly.graph_objects as go
from tkinter import *
from tkinter import scrolledtext

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')


stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]
    return tokens

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentences = sent_tokenize(text)
    sentiments = []

    for sentence in sentences:
        scores = sid.polarity_scores(sentence)
        sentiments.append(scores)

    return sentiments

def analyze_entities(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

def filter_entities_by_type(entities, entity_type):
    filtered_entities = [(entity, label) for entity, label in entities if label == entity_type]
    return filtered_entities

def plot_wordcloud(text, sentiment):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for {sentiment} Sentiment', fontsize=14)
    plt.show()

def analyze_and_visualize(text, entity_type=None):
    entities = analyze_entities(text)
    
    if entity_type:
        entities = filter_entities_by_type(entities, entity_type)
    
    sentiments = analyze_sentiment(text)
    
    # Plot sentiment timeline
    fig = go.Figure()
    for i, sent in enumerate(sentiments):
        fig.add_trace(go.Scatter(x=[i, i+1], y=[sent['compound'], sent['compound']], mode='lines+markers', name=f'Sentence {i+1}'))
    
    fig.update_layout(title='Sentiment Timeline Analysis',
                      xaxis_title='Sentence Number',
                      yaxis_title='Sentiment Score',
                      hovermode='closest',
                      showlegend=True)
    
    fig.show()
    
    # Generate word clouds for different sentiment categories
    positive_text = ' '.join([sent_tokenize(text)[i] for i, sent in enumerate(sentiments) if sent['compound'] >= 0])
    negative_text = ' '.join([sent_tokenize(text)[i] for i, sent in enumerate(sentiments) if sent['compound'] < 0])
    
    plot_wordcloud(positive_text, 'Positive')
    plot_wordcloud(negative_text, 'Negative')

def main():
    root = Tk()
    root.title('Sentiment Analysis Tool')

    frame = Frame(root)
    frame.pack(pady=20)

    label = Label(frame, text='Enter text to analyze sentiment:')
    label.pack(side=TOP)

    text_area = scrolledtext.ScrolledText(frame, wrap=WORD, width=50, height=10)
    text_area.pack(side=TOP)

    entity_type_label = Label(frame, text='Filter entities by type (optional):')
    entity_type_label.pack(side=TOP)

    entity_type_var = StringVar(root)
    entity_types = ['PERSON', 'ORG', 'GPE', 'DATE']  # Adjust as needed
    entity_type_var.set('')  # Default to no filtering

    entity_type_dropdown = OptionMenu(frame, entity_type_var, *entity_types)
    entity_type_dropdown.pack(side=TOP)

    def analyze_text():
        input_text = text_area.get('1.0', END)
        selected_entity_type = entity_type_var.get()
        analyze_and_visualize(input_text, selected_entity_type)

    analyze_button = Button(frame, text='Analyze Sentiment', command=analyze_text)
    analyze_button.pack(side=TOP)

    root.mainloop()

if __name__ == "__main__":
    main()
