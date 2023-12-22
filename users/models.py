from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_default_profile_picture():
    return "trainees/images/user.jpg"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username