#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from django.core.management.base import BaseCommand
from role.constants import ROLES
from role.models import Role


class Command(BaseCommand):
    help = '从constats.ROLES导入用户角色, 如果用户角色已经存在则修改原角色'

    def handle(self, *args, **options):

        for role in ROLES:
            name, description = role
            role, created = Role.objects.get_or_create(
                name=name, defaults={'description': ''}
            )
            if created:
                role.description = description
                role.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        'Successfully created role "%s"' % role.name)
                )
            else:
                if role.description != description:
                    role.description = description
                    role.save()
                    message = 'The role %s has been modified' % role.name
                else:
                    message = 'The role %s is same as before' % role.name
                self.stdout.write(self.style.WARNING(message))
