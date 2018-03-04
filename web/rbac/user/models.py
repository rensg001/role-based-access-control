from django.db import models
from role.models import Role

# Create your models here.

class User(models.Model):
    """用户"""

    name = models.CharField(max_length=16, unique=True,
                            null=False, db_index=True)
    password = models.CharField(max_length=64, null=False)
    solt = models.CharField(max_length=32, null=False)
    roles = models.ManyToManyField(Role, related_name='users')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
