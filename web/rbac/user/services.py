#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from common.mixins import CacheMixin
from user.models import User
from role.models import Role
from authorization.models import Authorization
from authorization.models import URLOperation


class UserService(CacheMixin):
    UserModel = User
    RoleModel = Role
    AuthorizationModel = Authorization
    URLOperationModel = URLOperation

    SOURCE_MODEL_MAP = {
        'url': [
            URLOperationModel,
            ('id', 'parent_id', 'url_prefix', 'operation', 'name')
        ]
    }

    def get_auth(self, user_id, prefix='auth'):
        self.set_prefix(prefix)
        user_authes = self.get(str(user_id))
        if user_authes:
            return user_authes
        user = self.UserModel.objects.prefetch_related(
            'roles__authorizations'
        ).get(pk=user_id)
        auth_resource_ids = {}
        for role in user.roles.all():
            for auth in role.authorizations.all():
                ids = auth_resource_ids.setdefault(auth.type, [])
                ids.append(auth.resource_id)

        auth_resources = {}
        for resource_type, resource_ids in auth_resource_ids.items():
            model, fields = self.SOURCE_MODEL_MAP.get(resource_type)
            if not model:
                continue
            resources = model.objects.filter(
                pk__in=resource_ids
            ).values(*fields)

            auth_resources[resource_type] = resources

        return auth_resources


user_service = UserService()