#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from django.conf.urls import url, include

from . import views

user_patterns = (
    [
        url('^auth/$', views.UserAuthAPIView.as_view(), name='user_roles')
    ],
    'user'
)

v1_urlpatterns = [url('^v1/', include(user_patterns, namespace='v1'))]

urlpatterns = v1_urlpatterns