pip install nltk
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize as wt 
from nltk.tokenize import sent_tokenize as st 
from nltk.corpus import stopwords as sw
from os import read
f = open('/textdata.txt')
sentence = f.read()
print(sentence)
# sentence = 'Ali is a boy, and he is 7 years old'
wordTokens = wt(sentence)
sentenceTokens = st(sentence)
# print(wordTokens[9])
print(wordTokens)
print(sentenceTokens)
print(sw.fileids())
englishCollection = set(sw.words('english'))
# words = ['ali','is','a','boy']
words = ['Lorem ','Ipsum ','is','dummy ']
result = [words for words in words if words not in englishCollection]
print(result)
from nltk.tokenize import word_tokenize as wt 
from nltk.tokenize import sent_tokenize as st 
from nltk.corpus import stopwords as sw 
from nltk.corpus import webtext
sentence = 'Ali is a boy, and he is 7 years old'
data = webtext.raw('')


