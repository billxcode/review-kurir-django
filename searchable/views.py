# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_questions' : latest_questions,
    }
    return HttpResponse(template.render(context, request))

def other_way_to_render_template(request):
    latest_questions = Question.objects.order_by('id')[:5]
    context = {'latest_questions':latest_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {'question': question}
    except Question.DoesNotExist:
        raise Http404('Question doesnt exist')
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "hello, you looking at category %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "hello you looking at vote view %s"
    return HttpResponse(response % question_id)
