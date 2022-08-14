#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import data_processing_oop


# In[2]:


# define stopwords
StopWords = stopwords.words("english")
StopWords.extend(["u","from"])


# In[3]:


# define a fuction to transform list and string
class transform:
    def __init__(self):
        return
# list to string
    def ListToString(list):
        string_words = ' '.join(list)
        return string_words

# string to list
    def StringToList(string):
        listRes = list(string.split(" "))
        return listRes


# In[4]:


class clean:
    def __init__(self):
        return

    def clean_text(text):
        
        #extract the tokens from string of characters 
        tokens = word_tokenize(text)
        
        # Remove the punctuations
        tokens = [word for word in tokens if word.isalpha()]
        
        # Lower the tokens
        tokens = [word.lower() for word in tokens]
        
        # Remove stopword
        tokens = [word for word in tokens if not word in StopWords]
        
        # Lemmatize
        lemma = WordNetLemmatizer()
        tokens = [lemma.lemmatize(word, pos="v") for word in tokens]
        tokens = [lemma.lemmatize(word, pos="n") for word in tokens]
        
        # list to string
        text = " ".join(tokens)
        return text

    # Extract nouns from speeches
    def nouns_extract(cont):
        nouns = []  # empty to array to hold all nouns
        cont = data_processing_oop.transform.StringToList(cont)
        
        for word, pos in nltk.pos_tag(cont):
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                nouns.append(word)
                string_nouns = data_processing_oop.transform.ListToString(nouns)
        return string_nouns

