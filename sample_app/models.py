from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)


class a(models.Model):
    phonenumber= models.IntegerField()

#class register(models.Model):
  #  name=models.CharField(max_length=100)
  #  mail=models.CharField(max_length=100)
  #  LOGIN = models.ForeignKey(login,default=1,on_delete=models.CASCADE)
  #  gender=models.CharField(max_length=10)

class register1(models.Model):
    name=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    image=models.CharField(max_length=100)
    language=models.CharField(max_length=100,default=1)

class notifi(models.Model):
    notification=models.CharField(max_length=100)
    date=models.CharField(max_length=200)

class book(models.Model):
    bookname = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)