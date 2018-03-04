from django.db import models

# Create your models here.

class Page(models.Model):
    """页面"""

    url = models.CharField(max_length=128, unique=True, null=False)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)