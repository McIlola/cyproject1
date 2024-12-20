import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cryptography.fernet import Fernet
from django.conf import settings

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    encrypted_address = models.BinaryField(null=True, blank=True)
    def set_address(self, address):
        fernet = Fernet(settings.ENCRYPTION_KEY)
        self.encrypted_address = fernet.encrypt(address.encode())
    def get_address(self):
        fernet = Fernet(settings.ENCRYPTION_KEY)
        return fernet.decrypt(self.encrypted_address).decode()
    def __str__(self):
        return f"{self.user.username}'s Profile"
