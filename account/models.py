from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from . import token_signal 

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
    # por algun motivo el admin no esta hasheando la password asi que esto es para hashearla
    def save(self, *args, **kwargs):
        if self.pk is not None:
            user = User.objects.get(pk=self.pk)
            if self.password != user.password:
                self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)