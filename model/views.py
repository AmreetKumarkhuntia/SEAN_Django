from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    # setntiment="positive"
    return HttpResponse("positive",content_type="application/json")