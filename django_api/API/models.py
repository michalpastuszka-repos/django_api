from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class UserProfile(models.Model):
    objects = None
    USER_TYPES = (
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ENTERPRISE', 'Enterprise')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    profile = models.CharField(choices=USER_TYPES, max_length=100, default='BASIC')

    def __str__(self):
        return f'Profile of {self.user.username}'

@receiver(post_save, sender=UserProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=UserProfile)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# one relation one to many
class ArticleCars(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class FuelType(models.Model):
    objects = None
    fuel = models.CharField(max_length=100)

    def __str__(self):
        return self.fuel


# one relation many to many
class CarModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    fuel_type = models.ManyToManyField(FuelType)

    def __str__(self):
        return self.name
