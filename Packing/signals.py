# yourapp/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OilPumpingDetails, ChangeLog
from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin
# Middleware and get_current_user function
from threading import local
from .middleware import get_current_user

_user = local()

User = get_user_model()

@receiver(post_save, sender=OilPumpingDetails)
def log_oil_pumping_details_changes(sender, instance, created, **kwargs):
    action = 'Created' if created else 'Updated'
    changes = instance.__dict__  # You can customize this to track specific changes
    user = get_current_user()  # Function to get the current user, see below
    print(f"log_oil_pumping_details_changes: user={user}, action={action}")
    ChangeLog.objects.create(
        user=user,
        model=sender.__name__,
        instance_id=instance.id,
        action=action,
        changes=str(changes)
    )

@receiver(post_delete, sender=OilPumpingDetails)
def log_oil_pumping_details_deletion(sender, instance, **kwargs):
    user = get_current_user()  # Function to get the current user, see below
    print(f"log_oil_pumping_details_deletion: user={user}, action=Deleted")
    ChangeLog.objects.create(
        user=user,
        model=sender.__name__,
        instance_id=instance.id,
        action='Deleted',
        changes='Deleted'
    )




