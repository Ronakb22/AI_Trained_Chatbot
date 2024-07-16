import json
import random
import pickle
import numpy as np
import billboard
import requests

import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

model = load_model('chatbot_model.h5')

def cleanup_sentences(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words, show_details = True):
    sentence_words = cleanup_sentences(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % word)
    return(np.array(bag))

def predict_class(sentence):
    p = bag_of_words(sentence, words, show_details = False)
    res = model.predict(np.array([p]), verbose = 0)[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key = lambda x: x[1], reverse = True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(ints, intents_json):
    tag = ints[0]['intent']
    
    if len(ints)==0:
        tag='noanswer'
    else:    
        tag=ints[0]['intent']
        
    if tag=='weather':
        api_key='987f44e8c16780be8c85e25a409ed07b'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = input("Enter city name : ")
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url) 
        x=response.json()
        print('Present temp.: ',round(x['main']['temp']-273,2),'celcius ')
        print('Feels Like:: ',round(x['main']['feels_like']-273,2),'celcius ')
        print(x['weather'][0]['main'])
        
    if tag=='song':
        chart=billboard.ChartData('hot-100')
        print('The top 10 songs at the moment are:')
        for i in range(10):
            song=chart[i]
            print(song.title,'- ',song.artist)
    
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(text):
    ints = predict_class(text)
    res = get_response(ints, intents)
    return res

while True:
    message = input("You: ")
    
    if message.lower() in ['quit', 'exit', 'close']:
        break
    elif any(str(a) + symbol + str(b) in message for a in [1,2,3,4,5,6,7,8,9,0] for b in [1,2,3,4,5,6,7,8,9,0] for symbol in ['*', '/', '-', '+', '**']):
        index = []
        for i in range(len(message)):
            if message[i].isnumeric():
                index.append(i)
        try:
            ans = eval(message[index[0]:index[-1]+1])
        except Exception as e:
            print("Bot: Error! ", e)
        else:
            print("Bot: ", ans)
    else:
        print("Bot: ", chatbot_response(message))