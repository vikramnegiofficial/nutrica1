from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.loginUser, name = "login"),
    path('logout/', views.logout ,name="logout"),
    # path('doc_reg', views.doc_reg ,name = 'doc_reg'),
    # path('doc_login', views.doc_login, name="doc_login"),
    path('patientdetails', views.patient_info, name="patient_info"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)