#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import copy

from django.core.management.base import BaseCommand
from django.db import transaction
from authorization.constants import AUTHORIZATIONS
from authorization.constants import TYPE_RESOURCE_MAP
from authorization.models import Authorization


class Command(BaseCommand):
    help = '从constats.AUTHORIZATIONS导入权限, 如果权限已经存在则修改原权限'

    def handle(self, *args, **options):
        # TODO update auth and resource when they already exist.

        with transaction.atomic():
            for auth in AUTHORIZATIONS:
                ResourceModel = TYPE_RESOURCE_MAP.get(auth['type'])
                resource = None
                if ResourceModel:
                    # 有具体的资源对象（非管理员权限）
                    parent = None
                    if auth['resource']['parent']:
                        parent = ResourceModel.objects.get(
                            **auth['resource']['parent']
                        )
                    resource_data = copy.deepcopy(auth['resource'])
                    resource_data.pop('parent')
                    resource_data['parent_id'] = parent.pk if parent else 0
                    resource, created = ResourceModel.objects.get_or_create(
                        **resource_data
                    )

                auth_obj, created = Authorization.objects.get_or_create(
                    name=auth['name'],
                    resource_id=resource.pk if resource else 0,
                    type=auth['type']
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            'Successfully created auth "%s"' % auth_obj.name)
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            'The auth %s is already exist' % auth_obj.name
                        )
                    )
