from django.shortcuts import render
from django.views import generic

from .models import Business

class IndexView(generic.ListView):
    model = Business
    paginate_by = 100
