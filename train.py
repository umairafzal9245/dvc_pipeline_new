import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import string 
import json 

df = pd.read_csv("data_processed.csv")

def text_process(title):
    
    nop = [char for char in title if char not in string.punctuation]
    nop = ''.join(nop)
    return [word for word in nop.split()]


# piplineTitle = Pipeline([
#     ('bow', CountVectorizer(analyzer=text_process)),
#     ('tfidf', TfidfTransformer()),
#     ('classifier', MultinomialNB()),
# ])
piplineTitle = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', LogisticRegression()),
])

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=123)

y_pred = piplineTitle.fit(X_train, y_train).predict(X_test)

confusion_matri = confusion_matrix(y_test, y_pred)

accuracy = (confusion_matri[0][0] + confusion_matri[1][1]) / (confusion_matri[0][0] + confusion_matri[0][1] + confusion_matri[1][0] + confusion_matri[1][1])

# Now print to file test
with open("metrics.json", 'w') as outfile:
        json.dump({"accuracy":accuracy}, outfile)
