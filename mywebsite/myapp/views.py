from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Homepage(request):
    return render(request, 'myapp/homepage.html')