from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
# class Likes(models.Model):
#     LIKE='L'
#     UNLIKE='N'
#     LIKE_CHOICE=[
#         LIKE, 'like',
#         UNLIKE, 'unlike'
#     ]
#     user=models.IntegerField(max_length=1, choices=LIKE_CHOICE, default="neutral")

class LikeItem(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey()