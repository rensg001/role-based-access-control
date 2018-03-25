#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from django.conf.urls import url, include

from . import views

user_patterns = (
    [
        url('^$', views.RoleAPIView.as_view(), name='role'),
    ],
    'role'
)

v1_urlpatterns = [url('^v1/', include(user_patterns, namespace='v1'))]

urlpatterns = v1_urlpatterns