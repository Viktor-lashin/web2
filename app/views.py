from django.shortcuts import render
from django.core.paginator import Paginator
import random

from django.http import HttpResponse

QUESTIONS = [
    {
        'id': i,
        'title': f'Question{i}',
        'content': f'lalalalala{i}',
        'tags': [list(['real', 'text', 'tag'])[random.randint(0, 2)], 'homework1'],
        'rating': random.randint(0, 100)
    } for i in range(100)
]

ANS = [
    {
        'id': i,
        'title': f'Question{i}',
        'content': f'lalalalala{i}',
        'tags': [list(['real', 'text', 'tag'])[random.randint(0, 2)], 'homework1'],
        'rating': random.randint(0, 100)
    } for i in range(2)
]

def paginate(objects_list, page, per_page=3):
    pageList = Paginator(objects_list, per_page)
    return pageList.page(page)

# Create your views here.
def indexNoRegister(request, page = 1):
    if page > (len(QUESTIONS)+2)//3:
        page = 1
    return render(request, 'index-noregister.html', {'questions': paginate(QUESTIONS, page, 3), 'pages': [page + x - 1 for x in range(3) if x + page - 1 > 0], 'reg': 'search'})


def indexRegister(request, page = 1):
    if page > (len(QUESTIONS)+2)//3:
        page = 1
    return render(request, 'index-register.html', {'questions': paginate(QUESTIONS, page, 3), 'pages': [page + x - 1 for x in range(3) if x + page - 1 > 0], 'reg': 'searchReg'})


def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'singleQuestion.html', {'question': item, 'reg': 'searchReg', 'ans': ANS})


def ask(request):
    return render(request, 'ask.html')


def errorAsk(request):
    return render(request, 'ask-error.html')


def logIn(request):
    return render(request, 'Log-in.html')

def errorLogIn(request):
    return render(request, 'Log-in-error.html')


def settings(request):
    return render(request, 'settings.html')
def settingsError(request):
    return render(request, 'settingsError.html')

def register(request):
    return render(request, 'register.html')
def registerError(request):
    return render(request, 'register-error.html')

def serchTag(request, tag, page = 1):
    return render(request, 'SearchTag-noregister.html', {'questions': paginate([Q for Q in QUESTIONS if tag in Q['tags']], page, 3), 'pages': [page + x - 1 for x in range(3) if x + page - 1 > 0], 'tag': tag, 'reg': 'search'})
def serchTagR(request, tag, page = 1):
    if page >= (len([Q for Q in QUESTIONS if tag in Q['tags']]))//3:
        page = 1
    return render(request, 'SearchTag-register.html', {'questions': paginate([Q for Q in QUESTIONS if tag in Q['tags']], page, 3), 'pages': [page + x - 1 for x in range(3) if x + page - 1 > 0], 'tag': tag, 'reg': 'searchReg'})
