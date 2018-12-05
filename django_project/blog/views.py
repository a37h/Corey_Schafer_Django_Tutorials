from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Lalala',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 1, 2018'
    },
    {
        'author': 'Lololo',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 2, 2018'
    }
]

def home(request):
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
