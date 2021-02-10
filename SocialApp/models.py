from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


def uploads(instance, filename):
    return 'SocialApp/image/{}'.format(filename)


class CreatedUpdated(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SocialIssue(CreatedUpdated):
    campaign_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=uploads)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.campaign_title


class BusinessPost(CreatedUpdated):
    company_name = models.CharField(max_length=255)
    campaign_title = models.CharField(max_length=255)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    image = models.ImageField(upload_to=uploads)
    address = models.CharField(max_length=50,null=True, blank=True)
    contact_no = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.campaign_title
