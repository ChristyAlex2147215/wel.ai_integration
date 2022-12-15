from django.db import models
from django.contrib.auth.models import User


SEMESTER_CHOICES = (
    ("Hackathon","Hackathon"),
    ("Treasure Hunt","Treasure Hunt"),
    ("Coding Debugging", "Coding Debugging"),
)

# Create your models here.
class Events(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=200,null=False,blank=True)
    image=models.ImageField(null=True,blank=True)
    createdBy=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=True)
    date=models.DateField(blank=True)
    time=models.TimeField(blank=True)
    address=models.TextField(max_length=200,null=False,blank=True)
    place=models.CharField(max_length=50,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    duration=models.IntegerField(null=True,blank=True,default=24)
    options=models.CharField(max_length =100,choices = SEMESTER_CHOICES,default='Hackathon',null=False,blank=True)
    
    def __str__(self):
        return str(self.name)

class Participants(models.Model):
    name=models.CharField(max_length=200,null=False,blank=True)
    id=models.AutoField(primary_key=True,editable=False)
    contact=models.BigIntegerField(null=False,blank=True)
    email=models.EmailField(max_length=254,null=False,blank=True)
    interests=models.TextField(max_length=300,null=False,blank=True)

    def __str__(self):
        return str(self.name)

    
