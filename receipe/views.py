from django.shortcuts import render
from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from myapp.models import Reecipe,Tag
from receipe import serializers




class  ReceipeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RecepiDeatailsSerialzier
    queryset = Reecipe.objects.all()
    authentication_classes =[TokenAuthentication]
    swagger_tags = ['Receipe']
    
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user= self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        if self.action =='list':
            return serializers.ReceipeSerualizer
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializers.save(user = self.request.user)
        
    
class Tagviewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        return self.queryset.filter(self.request.user).order_by('-name')