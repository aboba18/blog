from django.shortcuts import render

# Create your views here.
def index(req):

    return render(req, "blogapp/index.html")