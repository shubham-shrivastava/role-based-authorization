from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
class Article(models.Model):
    owner = models.ForeignKey(
        'auth.User', 
        related_name='articles',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True)
    content = models.CharField(max_length = 20000)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
