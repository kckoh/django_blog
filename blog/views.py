from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title' : 'Blog post 1',
        'content': 'first content',
        'date_posted': '26 Jan 2021'
    },
    {
        'author': 'Bob Kim',
        'title' : 'Blog post 2',
        'content': 'second content',
        'date_posted': '28 Jan 2021'
    }

]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)
# Create your views here.

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
