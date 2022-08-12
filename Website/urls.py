"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from Website.WebPage.views import home_Page
# from Website.WebPage.views import signup_page
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from WebPage import views
from django.conf.urls.static import static
from django.conf import Settings, settings
urlpatterns = [ 
    # path("qtn_submit/<int:pk>",views.qtn_submit,name="qtn-submit"),
    path("staff_page/",views.staff_page,name="staff-page"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("admissions/",views.school_admissions,name="school-admissions"),
    path("reg_courses/",views.add_courses,name="reg-courses"),
    path("reg_books/",views.add_books,name="reg-books"),
    path("reg_questions/",views.add_question,name="reg-questions"),
    path("view_questions/",views.view_questions,name="view-questions"),
    path("l",views.logout_f,name="logout"),
    path("",views.home_pag,name="home-pag"),
    path("hom",views.index.as_view(),name="home"),
    path("login/",views.UserLogin,name="login-page"),
    path("sign_up/",views.signup_page,name="sign-up-page"),
    path("reg_users/",views.add_users,name="reg-user-page"),
    path("view_users/",views.view_users,name="view-user-page"),
    path("view_courses/",views.view_courses,name="view_courses"),
    path("view_books/",views.view_books,name="view_books"),
    path("view_anns/",views.view_anns,name="view_anns"),
    path("dview_anns/",views.dview_anns,name="dview-anns"),
    path("dview_news/",views.dview_news,name="dview-news"),
    path("reg_view_posts/",views.reg_postings,name="reg_view_posts"),
    path("reg_news/",views.add_news,name="reg_news"),
    path("reg_anns/",views.Sadd_announcements,name="reg-announcements"),
    path("view_staffs/",views.view_staffs,name="view-staffs-page"),
    path("view_students/",views.view_students,name="view-students-page"),
    path("reg_staff/",views.Staff_Register,name="staff-reg-page"),
    path("reg_page/",views.Student_Reg,name="student-reg-page"),
    path("home_page/",views.home_Page),
    path("",include("WebPage.urls")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
