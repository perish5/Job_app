from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ROLES = (("0", "Admin"), ("1", "Employer"), ("2", "User"))
    role = models.CharField(max_length=1, choices=ROLES, default="2")
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "username", "role", "first_name", "last_name"
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    contact_num = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=False)
    prifile = models.ImageField(upload_to="jobs", null=True)