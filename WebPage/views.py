from datetime import date
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Post,Product,Student,Staff,Announcement,New,Posting,Book,Course,Question,multipleQuestion,DetailQuestion,MathQuestion
from django.views.generic.list import ListView
from .forms import ProductForm,StudentRegForm,PostingForm,AnnouncementForm,UserSignUpForm,UserLoginForm,QuestionsForm,QuestionsChoiceForm,QuestionsDetailForm,QuestionsMathsForm,BookForm,CourseForm
from django.contrib.auth.models import User,Permission
import os
from twilio.rest import Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
# import django.contrib.auth.context_processors.PermWrapper 
# from  django.contrib.auth.context_processors import PermWrapper 
# Create your views here.\
@login_required(login_url="/login/")
def home_pag(request):
    # if request.user.is_anonymous:
    #     if request.user.has_perm('auth.permission.Can_add_permission'):
    #         user=True
    # else:
    #     user=""
    #     print("not authorised")
    #     pass
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"home_page.html",{"user":user})
class index(ListView):
    model=Post
    template_name="home.html"
    context_object_name="Posts"
    paginate_by=5
    queryset=Post.objects.all()[:2]
def signup_page(request):
    
    if request.user.is_anonymous:

        if request.POST.get("sign_up_btn"):
            form=UserSignUpForm(request.POST)
            if form.is_valid:
                user_name=request.POST.get("username")
                first_name=request.POST.get("first_name")
                last_name=request.POST.get("last_name")
                email=request.POST.get("email")
                password=request.POST.get("password1")
                option=request.POST.get("option")

                if option=="as_staff":

                
                    try:
                        new_user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password,is_staff=True)
                    
                    
                    except:
                        new_user=None
                if option=="as_student":

                
                    try:
                        new_user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
                    
                    
                    except:
                        new_user=None
                    
                # form.is_staff=True
                # form.save()
                # new_user=authenticate(username=user_name,password=password)
                if new_user!=None:
                    login(request,new_user)
                    return redirect("/")
    else:
        return redirect("/")
    form=UserSignUpForm()
    return render(request,"sign_up.html",{"form":form})
def UserLogin(request):
    if request.user.is_anonymous:

        if request.POST.get("login_in_btn"):
            form=UserLoginForm(request.POST)
            if form.is_valid:
                user_name=request.POST.get("username")
                password=request.POST.get("password")
                
                loggedin_user=authenticate(request,username=user_name,password=password)
                if (loggedin_user != None):
                    # if loggedin_user.has_perm('auth.permission.Can_add_permission'):
                        # print("user has permission")

                        
                    login(request,loggedin_user)
                    return redirect("/")
                    # else:
                        # print("user has no permissions")
                else:
                    request.session["invalid_user"]=1
    else:
        return redirect("/")
    
    form=UserLoginForm()
    
    
        
    
    
    return render(request,"login.html",{"form":form})
class title(ListView):
    model=Post
    template_name="home.html"
    context_object_name="Posts"
    paginate_by=5
    def get_queryset(self,*args,**kwargs):
        return Post.objects.filter(title=self.kwargs.get("title"))

def home_Page(request):
    obj=Product.objects.all()
    return render(request,"base.html",{"products":obj})
def reg_Page(request):
    Myform =StudentRegForm()
    
    # if request.method=="POST":
    #     form =ProductForm(request.POST)

    #     if form.is_valid:
    #         form.save()
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"regForm.html",{"form":Myform,"user":user})
# @login_required
# @login_required(login_url="/sign_up/")
def Student_Reg(request):
    # ImgF=SImgForm(request.POST or None)
    if request.method=="POST":

        first_name=request.POST.get("First_name")
        second_name=request.POST.get("Second_name")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        Class=request.POST.get("Class")
        Stream=request.POST.get("Stream")
        Email=request.POST.get("emailid")
        Section=request.POST.get("Section")
        Parent_Name=request.POST.get("Parent_Name")
        Parent_contact=request.POST.get("Parent_contact")
        address=request.POST.get("Address")
        photo=request.FILES["MyPhoto"]
        # ImgF.save()

        s=Student(First_Name=first_name,Second_Name=second_name,Gender=gender,dob=dob,Class=Class,Stream=Stream,EmailID=Email,Section=Section,Parent_Name=Parent_Name,Parent_Contact=Parent_contact,Address=address,photo=photo)
        s.save()
    return render(request,"dstudentReg.html")

def Staff_Register(request):
    if request.method=="POST":
        staff_id=request.POST.get("staff_id")
        staff_name=request.POST.get("staff_name")
        gender=request.POST.get("gender")
        doj=request.POST.get("doj")
        designation=request.POST.get("designation")
        qualification=request.POST.get("qualification")
        mobile_no=request.POST.get("mobile_no")
        emailid=request.POST.get("emailid")
        address=request.POST.get("address")
        class_heading=request.POST.get("class_heading")

        Staff.objects.create(staff_id=staff_id,staff_name=staff_name,gender=gender,doj=doj,designation=designation,qualification=qualification,mobile_no=mobile_no,emailid=emailid,address=address,class_heading=class_heading)
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"dstaffReg.html",{"user":user})


def view_students(request):
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    
    if request.method=="POST":
        if request.POST.get("search")=="":
            students=Student.objects.all()
            return render(request,"dViewStudents.html",{"Students":students,"user":user})
        else:

            s=request.POST.get("search")
            students=Student.objects.all().filter(First_Name__icontains=s)    
            return render(request,"dViewStudents.html",{"Students":students,"user":user})
    else:
        students=Student.objects.all()
        return render(request,"dViewStudents.html",{"Students":students,"user":user})

    
def view_staffs(request):
    staffs=Staff.objects.all()    
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"dViewStaff.html",{"Staffs":staffs,"user":user})

def add_announcements(request):
    
    # if request.method=="POST":
        # if form.is_valid:
        #     form.save()
    # form=userForm_a(request.POST or None) 
    if request.method=="POST":
        form=AnnouncementForm(data=request.POST,files=request.FILES)    
        if form.is_valid:
            form.save()
            return render(request,"dAddAnns.html",{"form":form})
    else:
        form=AnnouncementForm()
        # user_name=request.POST.get("user_name")
        # title=request.POST.get("title")
        # image=request.FILES["image"]
        # body=request.POST.get("body")
        # date_posted=request.POST.get("dp")
        # form.save()

        # a=Announcement(title=title,image=image,body=body,date_posted=date_posted)
        # a.save()
        # a=Announcement.objects.get(id=)
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"dAddAnns.html",{"form":form,"user":user})

def Sadd_announcements(request):
    
    # if request.method=="POST":
        # if form.is_valid:
        #     form.save()
    # form=userForm_a(request.POST or None) 
    if request.method=="POST":
        form=AnnouncementForm(data=request.POST,files=request.FILES)    
        if form.is_valid:
            form.save()
            return render(request,"RegAnnouncements.html",{"form":form})
    else:
        form=AnnouncementForm()
        # user_name=request.POST.get("user_name")
        # title=request.POST.get("title")
        # image=request.FILES["image"]
        # body=request.POST.get("body")
        # date_posted=request.POST.get("dp")
        # form.save()

        # a=Announcement(title=title,image=image,body=body,date_posted=date_posted)
        # a.save()
        # a=Announcement.objects.get(id=)
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"RegAnnouncements.html",{"form":form,"user":user})

def add_news(request):
    # form=AnnouncementForm(request.POST or None)    
    # if request.method=="POST":
    #     if form.is_valid:
    #         form.save()
    # form=userForm_a(request.POST or None)
    if request.method=="POST":
        # user_name=request.POST.get("user_name")
        category=request.POST.get("category")
        title=request.POST.get("title")
        img=request.FILES["img"]
        body=request.POST.get("body")
        date_posted=request.POST.get("dp")
        # form.save()

        n=New(Category=category,Title=title,img=img,news_content=body,date_posted=date_posted)
        n.save()
        # a=Announcement.objects.get(id=)
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"dNewsReg.html",{"user":user})

def reg_postings(request):
    
    posts=Posting.objects.all()
    # print(posts.title)
    if request.method=="POST":
        form =PostingForm(data=request.POST,files=request.FILES)

        
        if form.is_valid:
            form.save()
            return render(request,"reg_posts.html",{"posts":posts,"form":form})
    else:
        form =PostingForm()
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"reg_posts.html",{"posts":posts,"form":form,"user":user})
def view_anns(request):
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    anns=Announcement.objects.all()
    return render(request,"view_anns.html",{"anns":anns,"user":user})
def view_books(request):
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    if request.method=="POST":
        if request.POST.get("search")=="":
            books=Book.objects.all()
            return render(request,"view_books.html",{"books":books,"user":user})
        else:

            b=request.POST.get("search")
            books=Book.objects.all().filter(Title__icontains=b)    
            return render(request,"view_books.html",{"books":books,"user":user})
    else:
        books=Book.objects.all()
        return render(request,"view_books.html",{"books":books,"user":user})
    # books=Book.objects.all()
    # return render(request,"view_books.html",{"books":books})

def view_courses(request):
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    if request.method=="POST":
        if request.POST.get("search")=="":
            courses=Course.objects.all()
            return render(request,"view_courses.html",{"courses":courses,"user":user})
        else:

            c=request.POST.get("search")
            courses=Course.objects.all().filter(Title__icontains=c)    
            return render(request,"view_courses.html",{"courses":courses,"user":user})
    else:
        courses=Course.objects.all()
        return render(request,"view_courses.html",{"courses":courses,"user":user})
    
def logout_f(request):
    logout(request)
    return redirect("/login/")        
    
def view_questions(request):
    qtns=multipleQuestion.objects.all()
    qtns2=DetailQuestion.objects.all()
    qtns3=MathQuestion.objects.all()
    # qt=qtns.option1
    # print(qtns.option1)
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"view_questions.html",{"qtns":qtns,"qtns2":qtns2,"qtns3":qtns3,"user":user})
def add_question(request):
    form1=QuestionsForm()    
    form2=QuestionsChoiceForm()
    form3=QuestionsDetailForm()
    form4=QuestionsMathsForm()
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    if request.POST.get("btn_f1"):
        if request.method=="POST":
            form1=QuestionsForm(request.POST)    
            if form1.is_valid:
                form1.save()
                redirect("/reg_questions/")
    if request.POST.get("btn_f2"):
        if request.method=="POST":
            form2=QuestionsChoiceForm(request.POST)    
            if form2.is_valid:
                form2.save()
                redirect("/reg_questions/")                
    if request.POST.get("btn_f3"):
        if request.method=="POST":
            form3=QuestionsDetailForm(request.POST)    
            if form3.is_valid:
                form3.save()
                redirect("/reg_questions/")    
    if request.POST.get("btn_f4"):
        if request.method=="POST":
            form4=QuestionsMathsForm(request.POST)    
            if form4.is_valid:
                form4.save()
                redirect("/reg_questions/")

    return render(request,"reg_questions.html",{"form1":form1,"form2":form2,"form3":form3,"form4":form4,"user":user})

def add_books(request):
    
    # if request.method=="POST":
        # if form.is_valid:
        #     form.save()
    # form=userForm_a(request.POST or None)
    if request.method=="POST":
        form=BookForm(data=request.POST,files=request.FILES)    
        if form.is_valid:
            form.save()
            return render(request,"RegBooks.html",{"form":form})
    else:
        form=BookForm()
        # user_name=request.POST.get("user_name")
        # title=request.POST.get("title")
        # image=request.FILES["image"]
        # body=request.POST.get("body")
        # date_posted=request.POST.get("dp")
        # form.save()

        # a=Announcement(title=title,image=image,body=body,date_posted=date_posted)
        # a.save()
        # a=Announcement.objects.get(id=)
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"RegBooks.html",{"form":form,"user":user})

def add_courses(request):
    
    # if request.method=="POST":
        # if form.is_valid:
        #     form.save()
    # form=userForm_a(request.POST or None)
    if request.method=="POST":
        form=CourseForm(data=request.POST,files=request.FILES)    
        if form.is_valid:
            form.save()
            return render(request,"RegCourses.html",{"form":form})
    else:
        form=CourseForm()
        # user_name=request.POST.get("user_name")
        # title=request.POST.get("title")
        # image=request.FILES["image"]
        # body=request.POST.get("body")
        # date_posted=request.POST.get("dp")
        # form.save()

        # a=Announcement(title=title,image=image,body=body,date_posted=date_posted)
        # a.save()
        # a=Announcement.objects.get(id=)
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"RegCourses.html",{"form":form,"user":user})


def school_admissions(request):
    cur=request.user
    
    if cur.is_superuser:
        user=True
    elif cur.is_staff:
 
        user=False
    else:
        user=None
    return render(request,"Admissions.html",{"user":user})

def dashboard(request):
    users=User.objects.all().count()
    students=Student.objects.all().count()
    staffs=Staff.objects.all().count()
    news=New.objects.all().count()
    anns=Announcement.objects.all().count()
    books=Book.objects.all().count()
    courses=Course.objects.all().count()

    return render(request,"dashboard.html",{"users":users,"students":students,"staffs":staffs,"news":news,"anns":anns,"books":books,"courses":courses})
def add_users(request):
    

    if request.POST.get("sign_up_btn"):
        form=UserSignUpForm(request.POST)
        if form.is_valid:
            user_name=request.POST.get("username")
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            email=request.POST.get("email")
            password=request.POST.get("password1")
            option=request.POST.get("option")

            if option=="as_staff":

                
                try:
                    new_user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password,is_staff=True)
                    
                    
                except:
                    new_user=None
            if option=="as_student":

                
                try:
                    new_user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
                    
                    
                except:
                    new_user=None
                    
                # form.is_staff=True
                # form.save()
                # new_user=authenticate(username=user_name,password=password)
            # if new_user!=None:
            #     login(request,new_user)
            #     return redirect("/")
    
    form=UserSignUpForm()
    
    return render(request,"dRegUsers.html",{"form":form})
def view_users(request):
    users=User.objects.all()
    return render(request,"dview_users.html",{"users":users})
def dview_anns(request):
    anns=Announcement.objects.all()
    return render(request,"dview_anns.html",{"anns":anns})
def dview_news(request):
    news=New.objects.all()
    return render(request,"dview_news.html",{"news":news})
def staff_page(request):
    return render(request,"staffpage.html",{})
