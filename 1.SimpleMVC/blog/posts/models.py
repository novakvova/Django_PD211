from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="defalut.jpg", blank=True)
    created_by =  models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
#    Student ivan = new Student("Іван Петрович");
#    Console.WriteLine(ivan);