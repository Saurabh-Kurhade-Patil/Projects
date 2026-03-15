import streamlit as st
import pickle
import string
import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

ps = PorterStemmer()


def preprocessing(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('packages/vectorizer.pkl', 'rb'))
model = pickle.load(open('packages/model.pkl', 'rb'))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter your message here...")

if st.button("Predict"):
    # 1. Preprocess
    transformed_sms = preprocessing(input_sms)
    # 2. Vectorize
    vector_sms = tfidf.transform([transformed_sms])
    # 3. Predict
    result = model.predict(vector_sms)
    # 4. Display
    if result[0] == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')
