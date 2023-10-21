from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    canegory_name = models.TextField(max_length=25)



class Post(models.Model):
    post_header = models.CharField(max_length=50)
    post_text = models.TextField(max_length=500)
    author = models.CharField(max_length=12)
    datetime = models.DateTimeField()
    category =  models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='no category')
    image = models.ImageField(upload_to="images/", default=None, null=True)

    def get_absolute_url(self):
        return reverse("post-details", args=[str(self.id)])


