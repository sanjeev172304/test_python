from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

#def index(request):
    #return HttpResponse("<h1>--- this is the home page </h1>")

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"