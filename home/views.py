from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>--- this is the home page </h1>")

