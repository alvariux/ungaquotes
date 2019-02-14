from django.shortcuts import render
from django.views import generic

from .models import Business

class BusinessList(generic.ListView):
    model = Business
    paginate_by = 100

class BusinessDetail(generic.DetailView):
    model = Business

class BusinessUpdate(generic.UpdateView):
    model = Business
