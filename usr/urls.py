from django.urls import path
from usr import views

app_name = 'usr'
urlpatterns = [
    path('create/' , views.CreateUserView.as_view() , name='create'),
    path('token/' , views.CreateToeknView.as_view(), name ='token'),
    path('manageuser/' , views.ManageUserView.as_view() ,name='manageuser'),
    
]
