from django.db import models
from django.conf import settings


# Create your models here.
from django.contrib.auth.models import(
    PermissionsMixin,
    BaseUserManager,
    AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self,email,password =None , **extra_fields):
        if not email:
            raise ValueError('USER MUST HAVE EMAIL ')
        user = self.model(email= self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff= True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
        
        
    
    
    
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    
    
    USERNAME_FIELD = 'email'
    
    
class Reecipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title =  models.CharField()
    description = models.TextField()
    time_minutes = models.IntegerField()
    prices = models.DecimalField(max_digits=5,decimal_places=2)
    link = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return self.title
    
     
    