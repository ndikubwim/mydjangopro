from django.urls import path
from .views import index, title
urlpatterns=[
    
    path("g/<str:title>",title.as_view(),name="title"),

]