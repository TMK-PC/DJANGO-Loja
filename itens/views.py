from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Itens

# Create your views here.

class ItensListView(ListView):
    model= Itens
    template_name = "itens.html"
    context_object_name = "itens"

class NewItemView(CreateView):
    model = Itens
    template_name = "new_item.html"
    fields = ['nome', 'tipo', 'descricao', 'foto']
    success_url = '/itens/'

class DeleteItemView(DeleteView):
    model = Itens
    success_url = '/itens/'
    template_name = 'delete_item.html'