from django.db import models

# Create your models here.
class userinfo(models.Model):
        username=models.CharField(max_length=50)
        password=models.CharField(max_length=50)
        email=models.EmailField()
        phonenumber=models.IntegerField()
        create_time=models.DateTimeField(auto_now_add=True)
        change_time=models.DateTimeField(auto_now=True)

class bloginfo(models.Model):
	headline=models.CharField(max_length=50)
	author=models.CharField(max_length=50)
	text=models.TextField()
	create_time=models.DateTimeField(auto_now_add=True)
        change_time=models.DateTimeField(auto_now=True)


