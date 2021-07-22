from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Post
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_post(sender, instance, created, **kwargs):
    print('Task Created')
    if created:
        Post.objects.create(user=instance)
        print('Task Created')
    else:
        instance.create_post.save()
        print('Task Created')
