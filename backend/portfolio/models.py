# portfolio/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    technology=models.CharField(max_length= 200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='projects/')
    gitlink = models.URLField(blank=True)
    projectlink = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"
