from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Question

def index(request):
    # On cree une variable et on interoge la table Question
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # On indique quel template loader
    #template = loader.get_template('polls/index.html')
    # On indique que quel contexte il s'agit
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    # On demande de rendre le template en question en fonction du contexte demande
    #return HttpResponse(template.render(context))

    #On peut faire plus court
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def zo (request, question_id):
    return  HttpResponse("Tu zoes sur la question %s." % question_id)

def za (request, a_id):
    return  HttpResponse("Tu as sur la question %s." % a_id )