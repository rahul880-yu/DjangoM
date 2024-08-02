from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def say_hello(request):
#     return HttpResponse("<h1>Ram Rajay </h1>")
def say_hello(request):
    x=1
    y=2
    return render(request, 'hello.html', {'name': 'Rahul'})