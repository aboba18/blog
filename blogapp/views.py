from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
# Create your views here.
def index(req):
    post_list = Post.objects.all()


    return render(req, "blogapp/index.html", context={"posts": post_list})

class PostDetailView(DetailView):
    template_name = "blogapp/post_detail.html"

    model = Post