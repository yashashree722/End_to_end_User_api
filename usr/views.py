from django.shortcuts import render

# Create your views here.
from rest_framework import generics,authentication ,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
 
from usr.serializers import UserSerializer,AuthTokenSerializer
    
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    
    
class CreateToeknView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes =[permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user
        
    