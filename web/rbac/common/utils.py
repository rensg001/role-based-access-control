#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os
import json

def read_json_file(file):
    """读取json文件内容"""
    assert os.path.exists(file)
    with open(file, mode='r') as f:
        data = f.read()
        return json.loads(data, encoding='utf8')
