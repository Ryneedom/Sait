"""sait URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from birja import views


urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.start),
    path('login', views.authenticate),
    path('logout', views.logout),
    path('register', views.register),
    path('applicants', views.applicant_index),
    path('applicants/mainpage', views.applicant_show),
    path('companies', views.company_index),
    path('companies/mainpage', views.company_show),
    path("companies/create", views.company_create),
    path("companies/edit/<int:id>/", views.company_edit),
    path("companies/delete/<int:id>/", views.company_delete),
    path('posts', views.post_index),
    path("posts/create", views.post_create),
    path("posts/edit/<int:id>/", views.post_edit),
    path("posts/delete/<int:id>/", views.post_delete),
    path('vacancies', views.vacancy_index),
]
