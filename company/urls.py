from django.urls import path, include
from . import views
urlpatterns = [
    path('create', views.create, name='create'),
    path('companydetail', views.companydetail, name='companydetail'),
]
