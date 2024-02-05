from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from abstract.models import AbstractModel

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if email is None:
            raise TypeError("Users must have an email")

        if password is None:
            raise TypeError("Users must have a password")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
