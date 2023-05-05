from django.db import models


class Contacts(models.Model):
    number = models.CharField(max_length=50)
    days = models.TextField()
    address = models.CharField(max_length=100)
    numbers = models.CharField(max_length=100)


class Doctors(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    image = models.ImageField(upload_to="")
    exp = models.CharField(max_length=200)
    likes = models.TextField(max_length=500)
    quote = models.CharField(max_length=200)


class About(models.Model):
    image = models.ImageField(upload_to="")
    descriptions = models.TextField(max_length=2000)
    number = models.CharField(max_length=100)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment_text = models.TextField(max_length=2000)
