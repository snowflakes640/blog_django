from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        "author" : "MTS",
        "title" : "Blog Post 1",
        "content" : "First post content",
        "date_posted" : "august 12, 2018"
    },
    {
        "author" : "Whoever 2",
        "title" : "Blog Post 2",
        "content" : "SEcond post content",
        "date_posted" : "august 15, 2018"
    },
    {
        "author" : "Whoever 3",
        "title" : "Blog Post 3",
        "content" : "Third post content",
        "date_posted" : "august 18, 2018"
    }
]

def home (request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)
    else:
        posts = Post.objects.none()  # or Post.objects.all() if you want to show all to anonymous users
    context = {
        "key": posts
    }
    return render(request, "blog_app/home.html", context)

def about (request):
    return render(request, "blog_app/about.html", {"title": "About"})

# # RUN 1
# def home(request):
#     return HttpResponse("<h1>Blog Home</h1>")

# def about(request):
#     return HttpResponse("<h1> About Page </h1>")
