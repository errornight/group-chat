from django.db import models
from django.contrib.auth.models import AbstractUser
import os
import random
import uuid
def generate_name(instance, filename):
   return f'profile_images/{instance.username}-{"".join([str(random.randint(0, 9)) for _ in range(8)])}.{os.path.splitext(filename)[1]}'

class User(AbstractUser):
    profile = models.ImageField(default='profile_images/Default.png', upload_to=generate_name, verbose_name='Profile Image')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    REQUIRED_FIELDS = []    # so there will not be Email in required fields.

    def __str__(self):
        return self.username