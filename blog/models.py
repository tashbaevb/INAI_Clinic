from django.db import models


class Slaider(models.Model):
    image = models.ImageField(upload_to="")
    image1 = models.ImageField(upload_to="")
    image2 = models.ImageField(upload_to="")
    number = models.CharField(max_length=100)


class News(models.Model):
    image = models.ImageField(upload_to="", null=True)
    image_advices = models.ImageField(upload_to="", null=True)
    image_advices1 = models.ImageField(upload_to="", null=True)


class Inai(models.Model):
    image = models.ImageField(upload_to="")
    title = models.TextField(max_length=1000)
    descriptions = models.TextField(max_length=3000)


class Foot(models.Model):
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    text = models.TextField(max_length=3000)


class Forman(models.Model):
    title = models.CharField(max_length=100)
    price = models.TextField()


class Forchildren(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=15)


class Clients(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    prichina = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
