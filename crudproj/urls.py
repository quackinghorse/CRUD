# crudproj/urls.py
from django.contrib import admin
from django.urls import path
from crudapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_management/', views.student_management, name='student_management'),
    path('studentapi/', views.student_api),
    path('studentapi/<int:pk>/', views.student_api),
]
