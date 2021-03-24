from django.db import models

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images')
    summary=models.CharField(max_length=3000)
    def __str__(self):
        return self.title


class Hub(models.Model):
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images')
    summary=models.CharField(max_length=3000)
    def __str__(self):
        return self.title
