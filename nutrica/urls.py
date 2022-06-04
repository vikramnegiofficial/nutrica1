from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('appointment', views.appointment, name="appointment"),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name="contact"),
    path('nutrition', views.nutrition , name="nutrition"),
    path('patient', views.patient , name="patient"),
    path('patient/<int:patient_id>/', views.singlepatient, name="singlepatient"),
    path('index',views.index,name="index"),  
    path('myaccount', views.myaccount, name="myaccount")
]