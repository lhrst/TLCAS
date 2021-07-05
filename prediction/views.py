from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    return render(request, 'prediction/index.html')

def result(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        
    txt = content.lower()
    for ch in '!"""“”#$%&()*+,-./:;<=>?@[\\]^_''{|}~1234567890':
        txt = txt.replace(ch, " ")
    ls = txt.split() 
    for i in range(1, len(ls)):
        word = ls[i]
        if word == 'embeddings' or word == 'networks' or word == 'languages' or word == 'models' or word == 'sentences' or word == 'phrases':
            ls[i] = word[:-1]
        elif word == 'nmt':
            if ls[i-1] == 'translation':
                ls[i] = ' '
            else:
                ls[i] = 'neural'
                ls.insert(i+1,'machine')
                ls.insert(i+2,'translation') 
        elif word == 'nlp':
            if ls[i-1] == 'processing':
                ls[i] = ' '
            else:
                ls[i] = 'natural'
                ls.insert(i+1,'language')
                ls.insert(i+2,'processing')          
    txt = " ".join(ls) 

    list =["language", "chinese", "english", "linguistic", "phrase", "sentence", "word embedding", "parser", "parsing", "acl", "summarization"]
    score_NLP = 0
    for word in list:
        if word in txt:
            print(word)
            score_NLP = score_NLP + (len(txt) - len(txt.replace(word,""))) // len(word)
    score_NLP = score_NLP * 3
    print(score_NLP)

    list =["object", "detection", "pixel", " pose ", " action ", "pattern", "recognition", "identification", "image", "segmentation", "computer vision"]
    score_REC = 0
    for word in list:
        if word in txt:
            print(word)
            score_REC = score_REC + (len(txt) - len(txt.replace(word,""))) // len(word)
    score_REC = score_REC * 1.2     
    print(score_REC)

    list =["reinforce", "learning", "network", "adversarial", "optimization", "graph", "regression", "polynomial", "gradient", "machine learning", "low rank", "convex"]
    score_LEA = 0
    for word in list:
        if word in txt:
            print(word)
            score_LEA = score_LEA + (len(txt) - len(txt.replace(word,""))) // len(word)
    print(score_LEA)

    list =["neural", "network", "extensive", "decision making", "markov", " ai ", "artificial", "learning", "tensor", "diagnos", "real time"]
    score_AI = 0
    for word in list:
        if word in txt:
            print(word)
            score_AI = score_AI + (len(txt) - len(txt.replace(word,""))) // len(word)
    print(score_AI)

    result = "AAAI, IJCAI"
    score = max(score_NLP, score_REC, score_LEA, score_AI)
    if score == score_AI:
        result = "AAAI, IJCAI"
    elif score == score_LEA:
        result= "ICML, NIPS"
    elif score == score_REC:
        result= "CVPR,ICCV"
    elif score == score_NLP:
        result= "ACL"

    return render(request, 'prediction/result.html', {'name': name, 'content': content,'author': author,'s': result})
