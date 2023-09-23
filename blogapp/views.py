from django.shortcuts import render
from .models import Post
# Create your views here.
def index(req):
    post_list = Post.objects.all()


    return render(req, "blogapp/index.html", context={"posts": post_list})