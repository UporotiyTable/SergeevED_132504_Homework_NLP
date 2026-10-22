#подготавливаю требуемые пакеты
import nltk
import string
import re
import pandas as pd
import transformers

#подгоняю таблицу с датасетом под удобный мне вид
"""
rev = pd.read_csv("C:/Users/user/Desktop/У_ёба/Инф/Ppract/reviews.csv", header=None, sep='\t')
for n in range(1002, 89001):
    rev = rev.drop(index=n, axis = 0)
    print(n)

x = range(0,len(rev[:,0]))
rev.insert(2, '2', x)
rev = rev.set_index('2')
rev.to_csv("reviews_shortened.csv", index = False, header=None, sep = '\t')
"""
rev = pd.read_csv("C:/Users/user/Desktop/У_ёба/Инф/Ppract/reviews_shortened.csv", header=None, sep='\t')

#Понижение регистра
def lowercase(text): 
    return text.lower() 

#Удаление чисел
def remove_num(text): 
    result = re.sub(r'\d+', '', text) 
    return result 
#Удаление пунктуации
def rem_punct(text): 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator)

#Исправление ошибок в тектсе
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
path_to_model = "ai-forever/RuM2M100-1.2B" 
 
model = M2M100ForConditionalGeneration.from_pretrained(path_to_model) 
tokenizer = M2M100Tokenizer.from_pretrained(path_to_model, src_lang="ru", tgt_lang="ru")

def deerror(text):
    encodings = tokenizer(text, return_tensors="pt") 
    generated_tokens = model.generate( 
            **encodings, forced_bos_token_id=tokenizer.get_lang_id("ru")) 
    answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return answer

#токенизация и лемматизация
from nltk.corpus import stopwords
from nltk.stem import wordnet 
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
lemma = wordnet.WordNetLemmatizer()

def lemmatization(text): 
    stop_words = set(stopwords.words("russian")) 
    
    word_tokens = word_tokenize(''.join(text)) 
    filtered_text = [word for word in word_tokens if word not in stop_words] 
    lemmas = [lemma.lemmatize(word, pos ='v') for word in filtered_text] 
    return lemmas

from pymorphy3 import MorphAnalyzer
from nltk import sent_tokenize, word_tokenize, regexp_tokenize

def tokenize_lemmas(sent, pat=r"(?u)\b\w\w+\b", morph=MorphAnalyzer()):
    return [morph.parse(tok)[0].normal_form 
            for tok in regexp_tokenize(' '.join(sent), pat)]

lemmatised = list()
lemmatised.append("lemmatised")
for x in range(len(rev.iloc[1:,0])):
    comment = rev.iloc[:,0][x]
    lc = lowercase(comment)
    rn = remove_num(lc)
    rp = rem_punct(rn)
    drr = deerror(rp)
    lem = lemmatization(drr)
    finl = tokenize_lemmas(lem)
    lemmatised.append(finl)
    print(x)
    
rev = rev.insert(2, '2', lemmatised)
rev.to_csv("reviews_lemmatised.csv", index = False, header=None, sep = '\t')

    
