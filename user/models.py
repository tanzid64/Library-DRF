from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractUser
from .constants import GENDER_TYPE
from .managers import UserManager
# Create your models here.
class User(AbstractUser, BaseModel):
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 15, default='')
    gender = models.CharField(max_length=8, default='', choices=GENDER_TYPE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    REQUIRED_FIELDS = ('email',)

    def __str__(self) -> str:
        return self.username