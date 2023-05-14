from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import pickle
from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# load the saved model
model = load_model('model/model/sentimental_analysis_model.h5')

# load the tokenizer used to preprocess the data
with open('model/model/tokenizer.pickle', 'rb') as f:
    tokenizer = pickle.load(f)


def index(request):
    return JsonResponse({"ServerStatus": "OK"})


def predict(request):
    if request.method == 'GET':
        # get the input review from the POST request
        input_review = request.GET.get('input_review')

        if(input_review!=None):
            # preprocess the input review
            input_seq = tokenizer.texts_to_sequences([input_review])
            input_padded = pad_sequences(input_seq, maxlen=100, padding='post', truncating='post')
            # make prediction using the trained model

            prediction = model.predict(input_padded)[0][0]
        else:
            prediction = -1

        if(prediction>0.5):
            sentiment="positive"
        elif(prediction>=0):
            sentiment="negative"
        else:
            sentiment="empty string was given"

        PredicitonNo=str(prediction)

        return JsonResponse({"Predictions":sentiment,
                             "PredictonNumber":PredicitonNo})
    else:
        return JsonResponse({"Predictions":"invalid method"})