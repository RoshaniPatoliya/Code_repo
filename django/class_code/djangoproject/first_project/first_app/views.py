from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecords

# Create your views here.

"""def home(request):
    my_dict={ 'insert_me':"Hello I am from views.py"}
    return render(request,'home.html', context=my_dict)"""

def index(request):
    return render(request,'index.html')
