from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageview(TemplateView):
    template_name = "home.html"
