from django.db import models
from authorization.models import Authorization

# Create your models here.


class Role(models.Model):
    """角色"""
    name = models.CharField(max_length=32, unique=True, null=False)
    authorizations = models.ManyToManyField(Authorization,
                                            related_name='roles')
    description = models.CharField(max_length=256, null=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)