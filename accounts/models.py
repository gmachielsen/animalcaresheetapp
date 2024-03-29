from django.db import models
from django.contrib.auth.models import User
from posts.models import Animal

# Create your models here.
class Profile(models.Model):

    GENDER_LIST = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nameOfUser = models.CharField(blank=True, null=True, max_length=120)
    image = models.ImageField(upload_to="media/avatars", default="avatars/anonymous.png")
    gender = models.CharField(max_length=1, choices=GENDER_LIST, blank=False, null=False)
    likes = models.ManyToManyField(Animal, related_name='liked_by')

    def __str__(self):
        return self.user.username + ' Profile'
