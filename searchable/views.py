# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_questions' : latest_questions,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    response = "Hello, you looking for detail %s"
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "hello, you looking at category %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "hello you looking at vote view %s"
    return HttpResponse(response % question_id)
