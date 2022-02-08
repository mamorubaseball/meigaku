from django.db import models
from django.conf import settings
from django.utils import timezone
from circle_accounts.models import Circles
from django.contrib.auth.models import (
User,BaseUserManager,AbstractBaseUser,PermissionsMixin
)

class Posts(models.Model):
    username = models.ForeignKey(
        Circles,on_delete=models.CASCADE
    )
    picture=models.FileField(upload_to='user/',null=True)
    title = models.CharField(max_length=200,null=True)
    title_url=models.URLField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=200,default='学生生活')

    def __str__(self):
        return self.title
