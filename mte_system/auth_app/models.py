from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.utils import timezone

class UserManager(BaseUserManager): 
    
    def create_user(self, username, kuet_id, first_name, last_name, email, password = None): 

        if not (username and kuet_id and first_name and last_name and email):
            raise ValueError("Required Field left empty.")

        user = self.model(
            username = username, 
            kuet_id = kuet_id, 
            first_name = first_name, 
            last_name = last_name, 
            email = email
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self, username, kuet_id, first_name, last_name, email, password = None): 

        user = self.create_user(
            username, 
            kuet_id, 
            first_name, 
            last_name, 
            email, 
            password
        )

        user.isStaff = True
        user.isSuperuser = True

        user.save(using=self._db)

        return user


class User_Profile(AbstractBaseUser, PermissionsMixin):

    kuet_id = models.CharField(
        max_length=9, 
        validators=[MinLengthValidator(9)], 
        help_text="Enter your 9 digit kuet_id", 
        unique=True
    )

    username = models.CharField(
        max_length=20, 
        unique=True,
    )

    image = models.ImageField(
        default="default.png", 
        upload_to="profile_pics"
    )

    first_name = models.CharField(
        max_length=50
    )

    last_name = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        max_length=50, 
        unique=True
    )

    isStaff = models.BooleanField(
        default = False
    )

    isSuperuser = models.BooleanField(
        default=False
    )

    isActive = models.BooleanField(
        default=True
    )

    date_joined = models.DateTimeField(
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = [
        'kuet_id', 
        'first_name', 
        'last_name', 
        'email'
    ]

    def __str__(self): 
        return self.username

    @property
    def is_staff(self): 
        return self.isStaff

    @property
    def is_superuser(self): 
        return self.isSuperuser

    @property
    def is_active(self): 
        return self.isActive

