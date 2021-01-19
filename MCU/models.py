from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=128)
    alias = models.CharField(max_length=128)
    movies = models.ManyToManyField('Movie')

    class Meta:
        ordering = ['alias']
        
    def __str__(self):
        return self.alias
    
class Platform(models.Model):
    title = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Phase(models.Model):
    title = models.CharField(max_length=64)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=128)
    release_date = models.DateField('release date', default=None, blank=True, null=True)
    url = models.URLField('url', max_length=128, blank=True, null=True)

    characters = models.ManyToManyField('Character')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['release_date']

    def __str__(self):
        return self.title


