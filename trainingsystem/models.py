from django.db import models
from django.contrib.auth.models import User
from .models import Product

class Product(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()

class ProductAccess(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Lesson(models.Model):
  title = models.CharField(max_length=100)
  video_link = models.URLField()
  duration = models.IntegerField()
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
class UserLesson(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  watched_time = models.IntegerField(default=0)
  status = models.BooleanField(default=False)
  last_watched_date = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return f"{self.user.username} - {self.lesson.title}"