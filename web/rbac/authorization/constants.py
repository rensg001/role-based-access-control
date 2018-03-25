#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from authorization.models import URLOperation


TYPE_RESOURCE_MAP = {
    'URL': URLOperation
}

AUTHORIZATIONS = [
    {
        'name': 'admin',
        'resource': {},
        'type': ''
    },
    {
        'name': 'user_auth',
        'resource': {
            'url_prefix': 'user/*/auth',
            'operation': 'GET',
            'name': 'user_auth',
            'parent': {}
        },
        'type': 'URL'
    }
]