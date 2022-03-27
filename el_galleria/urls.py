from django.urls import path

from el_galleria import views

urlpatterns = [
    path('', views.index, name="home")
]