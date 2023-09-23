from django.db import models

# Create your models here.
class Category(models.Model):
    canegory_name = models.TextField(max_length=25)



class Post(models.Model):
    post_header = models.CharField(max_length=50)
    post_text = models.TextField(max_length=120)
    author = models.CharField(max_length=12)
    datetime = models.DateTimeField()
    category =  models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='no category')

