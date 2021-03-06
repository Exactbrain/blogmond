from django.db import models
from django.utils import timezone


class Breaking(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title
        
class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title
        
class Series(models.Model):
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='images/')
	body = models.TextField()
	
	def __str__(self):
		return self.title
    
    
class Tv(models.Model):
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField(default=timezone.now)
	video = models.FileField(upload_to='videos/', null=True, verbose_name="")
	body = models.TextField()
	
	def __str__(self):
		return self.title

