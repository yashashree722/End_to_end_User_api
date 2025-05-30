
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from receipe import views

router = DefaultRouter()
router.register('receipe/' ,views.ReceipeViewset)

# app_name
urlpatterns = [
    path('' , include(router.urls)),
]



