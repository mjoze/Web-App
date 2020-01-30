from django.shortcuts import render

posts = [
    {
        'author': 'MJ',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 01, 2020'
    },
    {
        'author': 'MJ',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'January 30, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
