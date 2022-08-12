from django import forms
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms import fields, widgets
from .models import Posting, Product,Student,Announcement,Question,multipleQuestion,DetailQuestion,MathQuestion,Book,Course
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Product
        fields=["title","price","description","Like"]
class StudentRegForm(forms.Form):
    student_name=forms.TextInput(attrs={"class":"form-control"})
    student_id=forms.NumberInput(attrs={"class":"form-control"})
    Class=forms.TextInput(attrs={"class":"form-control"})
# class AnnouncementForm(forms.ModelForm):
    
#     class Meta:
#         model=Announcement
#         fields="__all__"
#         widgets={
            
#             "title":forms.TextInput(attrs={"class":"form-control"}),
#             "body":forms.Textarea(attrs={"class":"form-control"}),
#             "date_posted":forms.DateInput(attrs={"class":"form-control"})
            


        # }
# class SImgForm(forms.ModelForm):
#     class Meta:
#         model=Student
#         fields=["photo"]
# class userForm_a(forms.ModelForm):
#     class Meta:
#         model=Announcement
#         fields=["A_user"]

class PostingForm(forms.ModelForm):
    
    class Meta:
        model=Posting
        fields=["author","image","title","body","date_posted"]
        widgets={"author":forms.Select(attrs={"class":"form-control"}),"title":forms.TextInput(attrs={"class":"form-control"}),"body":forms.Textarea(attrs={"class":"form-control"}),"image":forms.FileInput(attrs={"class":"form-control"}),"date_posted":forms.DateInput(attrs={"class":"form-control"})}
class AnnouncementForm(forms.ModelForm):
    
    class Meta:
        model=Announcement
        fields=["author","title","image","body","date_posted"]
        widgets={"author":forms.Select(attrs={"class":"form-control"}),"title":forms.TextInput(attrs={"class":"form-control"}),"body":forms.Textarea(attrs={"class":"form-control"}),"image":forms.FileInput(attrs={"class":"form-control","enctype":"multipart/form-data"}),"date_posted":forms.DateInput(attrs={"class":"form-control"})}
class CourseForm(forms.ModelForm):
    
    class Meta:
        model=Course
        fields=["Category","Title","img_cover","Course_Main_Content","book_pdf"]
        widgets={"Category":forms.TextInput(attrs={"class":"form-control"}),"Title":forms.TextInput(attrs={"class":"form-control"}),"Course_Main_Content":forms.Textarea(attrs={"class":"form-control"}),"img_cover":forms.FileInput(attrs={"class":"form-control","enctype":"multipart/form-data"}),"book_pdf":forms.FileInput(attrs={"class":"form-control","enctype":"multipart/form-data"})}        
class BookForm(forms.ModelForm):
    
    class Meta:
        model=Book
        fields=["Class","Subject","Title","book_pdf"]
        widgets={"Class":forms.TextInput(attrs={"class":"form-control"}),"Subject":forms.TextInput(attrs={"class":"form-control"}),"Title":forms.TextInput(attrs={"class":"form-control"}),"book_pdf":forms.FileInput(attrs={"class":"form-control"})}

class UserSignUpForm(UserCreationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({
            "class":"form-control"
        })
        self.fields["password2"].widget.attrs.update({
            "class":"form-control"
        })
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]
        widgets={"username":forms.TextInput(attrs={"class":"form-control"}),"first_name":forms.TextInput(attrs={"class":"form-control"}),"last_name":forms.TextInput(attrs={"class":"form-control"}),"email":forms.EmailInput(attrs={"class":"form-control"})}
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({
            "class":"form-control"
        })
        self.fields["username"].widget.attrs.update({
            "class":"form-control"
        })
        
    class Meta:
        model=User
        fields=["username","password"]
class QuestionsForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=["author","Class","Subject","Topic","Question","date_posted"]
        widgets={
            "author":forms.Select(attrs={"class":"form-control"}),
            "Class":forms.TextInput(attrs={"class":"form-control"}),
            "Subject":forms.TextInput(attrs={"class":"form-control"}),
            "Topic":forms.TextInput(attrs={"class":"form-control"}),
            "Question":forms.Textarea(attrs={"class":"form-control"}),
            "date_posted":forms.DateInput(attrs={"class":"form-control"})
        }
class QuestionsChoiceForm(forms.ModelForm):
    class Meta:
        model=multipleQuestion
        fields=["Question","Option_1","Option_2","Option_3","Option_4","Answer"]
        widgets={
            "Question":forms.Select(attrs={"class":"form-control"}),
            "Option_1":forms.TextInput(attrs={"class":"form-control"}),
            "Option_2":forms.TextInput(attrs={"class":"form-control"}),
            "Option_3":forms.TextInput(attrs={"class":"form-control"}),
            "Option_4":forms.TextInput(attrs={"class":"form-control"}),
            "Answer":forms.TextInput(attrs={"class":"form-control"})
        }
class QuestionsDetailForm(forms.ModelForm):
    class Meta:
        model=DetailQuestion
        fields=["Question","Answer"]
        widgets={
            "Question":forms.Select(attrs={"class":"form-control"}),
            
            "Answer":forms.Textarea(attrs={"class":"form-control"})
        }        
class QuestionsMathsForm(forms.ModelForm):
    class Meta:
        model=MathQuestion
        fields=["Question","Answer"]
        widgets={
            "Question":forms.Select(attrs={"class":"form-control"}),
            
            "Answer":forms.NumberInput(attrs={"class":"form-control"})
        }