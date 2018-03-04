from django.db import models

# Create your models here.


class Authorization(models.Model):
    """权限"""

    class Meta:
        unique_together = (("source_id", "type"),)

    name = models.CharField(max_length=32, unique=True, null=False)
    source_id = models.IntegerField()
    type = models.CharField(max_length=10, null=False)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)