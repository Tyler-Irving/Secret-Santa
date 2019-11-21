from django.shortcuts import render
from django.views import generic
from S_Sv1.models import Person

# Create your views here.
class PeopleListView(generic.ListView):
    model = Person
    context_object_name = "list"
    template_name = "home.html"
