from django.db import models
from django.contrib.auth.models import User
from .cohort import Cohort
from django.db.models.signals import post_save
from django.dispatch import receiver
# Cannot define user in a Django app, so Instructors will become
# users using Django's built in User model
class Instructor(models.Model): 
    # Instructors are the user, therefore a one to one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slack_handle = models.CharField(max_length=50, null=True)
    specialty = models.CharField(max_length=50, null=True)
    # cohort_id value is a foreign key associated with the ID of cohort
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, null=True)

# When a user is created, a matching Instructor is created
@receiver(post_save, sender=User)
def create_instructor(sender, instance, created, **kwargs):
    if created: 
        Instructor.objects.create(user=instance)
# When a user is saved, a matching Instructor is saved
@receiver(post_save, sender=User)
def save_instructor(sender, instance, **kwargs):
    instance.instructor.save()