from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='moviepic')
    desc=models.TextField()

    def __str__(self) :
        return self.name
