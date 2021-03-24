from django.shortcuts import render
from .models import Post
# Create your views here.
def main(request):
    posts=Post.objects
    return render(request,'posts/posts.html',{"posts":posts})
