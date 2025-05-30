
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from receipe import views

app_name = 'receipe'

router = DefaultRouter()
router.register('recepies' ,views.ReceipeViewset)
router.register('tags' , views.Tagviewset)

# app_name
urlpatterns = [
    path('' , include(router.urls)),
]



