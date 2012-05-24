#! /usr/bin/python
# -*- coding: utf-8 -*-
# Created by Syno Tech.
# User: Syno-Frank
# Date: 5/3/12
# Time: 4:47 PM
# Author: Lihuashan, 8153467.qq.com
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

path = default_storage.save('/shinetec-42a57a/TexasFile/CountySet36/Martin/images/abc', ContentFile('new content'))
print path

default_storage
print default_storage.size(path)

print default_storage.open(path).read()


default_storage.delete(path)
print default_storage.exists(path)

print default_storage.url