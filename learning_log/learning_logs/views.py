from django.shortcuts import render
from .models import Topic 

# Create your views here.

def index(request):
    """Página principal do learning_log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by("dte_added")  # armazena a lista de tópicos na variável 'topics'
    context = {'topics': topics}  # passa 'topics' para o contexto
    return render(request, 'learning_logs/topics.html', context)