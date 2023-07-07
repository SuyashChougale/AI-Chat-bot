f = open(r"data.txt","r",errors="ignore")
df = f.read()
df.lower()


from nltk.tokenize import word_tokenize,sent_tokenize
import string
sent_tokens = sent_tokenize(df)
sent_tokens2 = []
for sentence in sent_tokens:
    sentence = sentence.translate(str.maketrans('','',string.punctuation))
    sent_tokens2.append(sentence)
# sent_tokens = []
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from nltk.corpus import stopwords
stopword = set(stopwords.words('english'))
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
for j in range(len(sent_tokens2)) :
    words = word_tokenize(sent_tokens2[j])
    for i in range(len(words)):
        words[i] = stemmer.stem(words[i])
        words[i] = lemmatizer.lemmatize(words[i])
        if words[i] not in stopword:
            continue
        else:
            words[i] = '' 
    sent_tokens2[j] = ' '.join(words)
# print(sent_tokens[0])
# print(sent_tokens2[0])
# print(sent_tokens2)
import random
import numpy as np
def greet(user_reponse):
    
    greet_inputs = ["hello","hi","whatss up?","how are you?"]
    greet_response = ["hello","I am good,What about you?","Hi"]
    user_words = word_tokenize(user_reponse.lower())
    for word in user_words:
        if word.lower() in greet_inputs:
            return(random.choice(greet_response))
    
# print(greet("hello"))
def quit(user_response):
    quit_inputs = ["quit","bye"]
    quit_response = ["Okay,Have a Nice Day!"]
    thanks_inputs = ["thanks" , "thank" ]
    user_words = word_tokenize(user_response.lower())
    for word in user_words:
        if word.lower() in thanks_inputs:
            return "Your Welcome"
        if word.lower() in quit_inputs:
            return random.choice(quit_response)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def response(user_response):
    bot_response = ''
    sent_tokens.append(user_response.lower())
    TfidfVec = TfidfVectorizer(stop_words='english' )
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1],tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    a = sorted(flat)
    req_tfidf = a[-2]

    if req_tfidf == 0:
        bot_response = bot_response+"I am sorry. I can't answer everything.I Have definite knowledge."
        sent_tokens.remove(user_response)
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        sent_tokens.remove(user_response.lower())
        return bot_response
# print(response("what is universe"))

    # print(vals)

# response("Hey I am Suyash!")
flag = True
while flag==True:
    
    user_input = input().lower()
    words = word_tokenize(user_input)
    print("user : ",user_input)
    print("Bot : ",end="")
    if (quit(user_response=user_input) != None):
        print(quit(user_response=user_input))
        flag = False
    else:
        if(greet(user_input)!=None):
                  print(greet(user_input))
        else:
                print(response(user_input))
    




