from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response=requests.get('https://jsonplaceholder.typicode.com/users').json()
    return render(request,'info.html',{'response':response})

    
