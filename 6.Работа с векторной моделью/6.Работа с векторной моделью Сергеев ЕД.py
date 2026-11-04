import numpy as np
import pandas as pd
import re
import nltk
import string

#Чтение датасета с текстом
df = pd.read_csv("C:\У_ёба\Инф\Ppract\zamok.test", encoding='UTF8', sep="\t", header = None)
df.head()

from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('russian'))
#удаляю стопслова из текстов
def stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])
# Удаление эмодзи
def emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)
#Удаление URL
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)
from bs4 import BeautifulSoup

#Лемматизация
from pymorphy3 import MorphAnalyzer
from nltk import sent_tokenize, word_tokenize, regexp_tokenize

def tokenize_lemmas(sent, pat=r"(?u)\b\w\w+\b", morph=MorphAnalyzer()):
    return [morph.parse(tok)[0].normal_form 
            for tok in regexp_tokenize(sent, pat)]

df['text_ready']  = df[0].str.lower()
df['text_ready'] = df['text_ready'].str.replace('\d+', '') 
df['text_ready'] = df['text_ready'].str.replace('[^\w\s\`]','')
df["text_ready"] = df["text_ready"].apply(stopwords)
df['text_ready'] = df['text_ready'].apply(emoji)
df['text_ready'] = df['text_ready'].apply(remove_urls)
df["text_ready"] = df["text_ready"].map(lambda x: " ".join(tokenize_lemmas(x)))
df['text_ready'] = df['text_ready'].str.replace('замо', 'замкдн')
df['text_ready'] = df['text_ready'].str.replace('за мокнуть', 'замкдв')
df[['text_ready']].head()

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

w2v_model = Word2Vec(
    min_count=10,
    window=4,
    vector_size=300,
    negative=10,
    alpha=0.03,
    min_alpha=0.0007,
    sample=6e-5,
    sg=0)

from nltk.tokenize import sent_tokenize
from gensim.utils import simple_preprocess

class MySentences(object):
    def __init__(self, docs):
        self.corpus = docs
    def __iter__(self):
        for doc in self.corpus:
            doc_sentences = sent_tokenize(doc)
            for sent in doc_sentences:
                yield simple_preprocess(sent) 

sentences = MySentences(df['text_ready'].tolist())

w2v_model.build_vocab(sentences)

w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=4, report_delay=1)

w2v_model.save("C:\У_ёба\Инф\Ppract\w2v_model")