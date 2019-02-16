from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Business
from .forms import BusinessForm

class BusinessList(generic.ListView):
    model = Business
    paginate_by = 100

class BusinessDetail(generic.DetailView):
    model = Business

class BusinessCreate(generic.CreateView):
    model = Business
    form_class = BusinessForm
    template = 'business/business_form.html'
    success_url = reverse_lazy('business:list')

class BusinessUpdate(generic.UpdateView):
    model = Business
    form_class = BusinessForm
    template = 'business/business_form.html'
    success_url = reverse_lazy('business:list')

class BusinessDelete(generic.DeleteView):
    model = Business    
    success_url = reverse_lazy('business:list')
