from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DecimalField, TextField
from django.db.models.fields.files import ImageField
from django.http import request
import datetime
from django.contrib.auth.models import User
# from django import models
# Create your models here.

import os
from twilio.rest import Client

class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=500)
    price=models.DecimalField(max_digits=1000,decimal_places=4,default=0.0)
    description=models.TextField()
    Like=models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Student(models.Model):
    First_Name=models.CharField(max_length=500)
    Second_Name=models.CharField(max_length=500)
    Gender=models.CharField(max_length=500)
    dob=models.DateField(default=datetime.datetime.now())
    Class=models.CharField(max_length=500)
    Stream=models.CharField(max_length=500)
    EmailID=models.EmailField()
    Section=models.CharField(max_length=500)
    Parent_Name=models.CharField(max_length=500)
    Parent_Contact=models.CharField(max_length=500)
    Address=models.CharField(max_length=500)
    photo=models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.First_Name+"-"+self.Second_Name
    
class Staff(models.Model):
    staff_id=models.CharField(max_length=500)
    staff_name=models.CharField(max_length=500)
    gender=models.CharField(max_length=500)
    doj=models.DateField()
    designation=models.CharField(max_length=500)
    qualification=models.CharField(max_length=500)
    mobile_no=models.CharField(max_length=500)
    emailid=models.EmailField()
    address=models.CharField(max_length=500)
    class_heading=models.CharField(max_length=500)

    def __str__(self):
        return self.staff_name
class profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    web_url=models.CharField(max_length=500,default="")
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profiles/")

    def __str__(self):
        return str(self.user)

    



class Posting(models.Model):
    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    image=models.ImageField(null=True,blank=True,upload_to="images/Postings")
    body=models.TextField()
    date_posted=models.DateField(default=datetime.datetime.now())
    def __str__(self):
        return self.title

class Announcement(models.Model):
    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    image=models.ImageField(null=True,blank=True,upload_to="images/announcements")
    body=models.TextField()
    date_posted=models.DateField(default=datetime.datetime.now())
    def __str__(self):
        return self.title

class Question(models.Model):
    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    Class=models.CharField(max_length=500)
    Subject=models.CharField(max_length=500)
    Topic=models.CharField(max_length=500)
    # Sub_Topic=models.CharField(max_length=500)
    Question=models.TextField()
    # Answer=models.CharField(max_length=1000)
    # image=models.ImageField(null=True,blank=True,upload_to="images/Questions")
    date_posted=models.DateField(default=datetime.datetime.now())
    def __str__(self):
        return "Question : "+self.Question

class New(models.Model):
    Category=models.CharField(max_length=500)
    Title=models.CharField(max_length=500)
    img=models.ImageField(null=True,blank=True,upload_to="images/News")
    news_content=TextField()
    date_posted=models.DateField(default=datetime.datetime.now())
    def __str__(self):
        return self.Title

class Course(models.Model):
    Category=models.CharField(max_length=500)
    Title=models.CharField(max_length=500)
    img_cover=models.ImageField(null=True,blank=True,upload_to="images/Courses")
    Course_Main_Content=TextField()
    book_pdf=models.FileField(null=True,upload_to="Course_Books/")

    def __str__(self):
        return self.Title 

class Book(models.Model):
    Class=models.CharField(max_length=500)
    Subject=models.CharField(max_length=500)
    Title=models.CharField(max_length=500)
    book_pdf=models.FileField(null=True,upload_to="Books/")
    def __str__(self):
        return self.Title
    
class Score(models.Model):
    result=models.PositiveIntegerField()
    def __str__(self):
        return str(self.result)
    def save(self,*args,**kwargs):
        if self.result<70:
            


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
            account_sid = "ACb43d55f683342fc8c159311e688147cb"
            auth_token = "79f6e4519d3088bac50ccc283907ee0b"
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body=f"Your Current Result is bad-{self.result}",
                                
                                from_='+16612470253',
                                to='+250782704742'
                            )

            print(message.sid)
        return super().save(*args,**kwargs)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

class multipleQuestion(models.Model):
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    Option_1=models.CharField(max_length=1000)
    Option_2=models.CharField(max_length=1000)
    Option_3=models.CharField(max_length=1000)
    Option_4=models.CharField(max_length=1000)
    Answer=models.IntegerField(max_length=1000)

    def __str__(self):
        return f"Choices[{self.Option_1},{self.Option_2},{self.Option_3},{self.Option_4}]"
class DetailQuestion(models.Model):
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    Answer=models.TextField()

    def __str__(self):
        return f"Question : {self.Question} and Answer : {self.Answer}"        
class MathQuestion(models.Model):
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    Answer=models.IntegerField(max_length=1000)

    def __str__(self):
        return f"Question : {self.Question} and Answer : {self.Answer}"        