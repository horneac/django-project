from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='movies'),
    path('details/<int:id>', views.details, name='details')
]