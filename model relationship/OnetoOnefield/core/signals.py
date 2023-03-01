from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from core.models import Page


@receiver(post_delete, sender=Page)
def post_delete(sender, instance, using, origin, *args, **kwargs):
    print('sender ', sender)
    print('instance ', instance)
    print('using ', using)
    print('origin ', origin)
    print('args ', args)
    print('kwargs ', kwargs)
    # In instance have page model every field
    print(instance.user)  # This user is object of User model
    print(instance.page_name)
    print(instance.page_category)
    instance.user.delete()
