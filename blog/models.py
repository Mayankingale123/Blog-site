from time import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#data base 
# each class is its own table
# each attribute is a different field in database 

class Post(models.Model):
    title = models.CharField(max_length=10000)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

#corey full video on str
    def __str__(self):
        return self.title
   
  #**** why reverse not redirect 
  # when we submit new post we reverse to that post view 
    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'pk':self.pk})