from django.db import models

# Create your models here.
class Movies(models.Model):
    movieName=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.movieName