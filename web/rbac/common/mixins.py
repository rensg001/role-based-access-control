#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from django.core.cache import cache

class CacheMixin(object):
    def __init__(self):
        self.prefix = ''
        self.cache = cache

    def set_prefix(self, prefix='prefix'):
        self.prefix = prefix

    def get_cache_key(self, key):
        assert key and self.prefix

        key = '{}:{}'.format(self.prefix, key)
        return key

    def set(self, key, value, expire=5):
        cache_key = self.get_cache_key(key)
        self.cache.set(cache_key, value, expire)

    def get(self, key):
        cache_key = self.get_cache_key(key)
        return self.cache.get(cache_key)
