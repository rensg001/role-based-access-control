from django.db import models

# Create your models here.


class Authorization(models.Model):
    """权限"""

    class Meta:
        unique_together = (("resource_id", "type"),)

    name = models.CharField(max_length=32, unique=True, null=False)
    resource_id = models.IntegerField()
    type = models.CharField(max_length=10, null=False)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)


class URLOperation(models.Model):
    """资源操作"""

    class Meta:
        unique_together = (("url_prefix", "operation"), )

    url_prefix = models.CharField(max_length=128, unique=True, null=False)
    operation = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=20, null=False)
    # 父资源操作id
    parent_id = models.IntegerField()
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)