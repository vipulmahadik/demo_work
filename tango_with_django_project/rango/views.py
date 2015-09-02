from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("About page")
