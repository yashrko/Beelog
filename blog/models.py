from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    article_image=models.ImageField(default='articleDefault.jpg',upload_to="article_image")
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("blog-update-view", kwargs={"pk": self.pk})
    