from django.shortcuts import render
from django.http import HttpResponse

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
    context = {
        "key" : posts
    }
    return render(request, "blog_app/home.html", context)

def about (request):
    return render(request, "blog_app/about.html", {"title": "About"})

# # RUN 1
# def home(request):
#     return HttpResponse("<h1>Blog Home</h1>")

# def about(request):
#     return HttpResponse("<h1> About Page </h1>")
