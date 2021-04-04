from django.shortcuts import render,redirect
from chatterbot import ChatBot
from django.http import HttpResponse
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

# Create your views here.
chatbot = ChatBot(
    'CoviBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

 # Training with Personal Ques & Ans

train_data_personal = open('train_data/personal_ques.txt',encoding="utf8").read().splitlines()

train_data = train_data_personal

trainer = ListTrainer(chatbot)
trainer.train(train_data)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)
def get_bot_response(request):
    userText =request.GET.get('msg')
    return HttpResponse(chatbot.get_response(userText))
def main(request):
    return render(request,'main.html')

def t2(request):
    r2=request.GET.get('dark')
    print(r2)
    if r2=='0':
        print("0")
        s=0
        request.session['s']=s
        print(request.session['s'])
        return HttpResponse('SUCCESS')
    else:
        print("1")
        s=1
        request.session['s']=s
        print(request.session['s'])
        return HttpResponse('SUCCESS')
def t1(request):
    print('ok')
    return render(request,'main.html',{'k': request.session['s']})

