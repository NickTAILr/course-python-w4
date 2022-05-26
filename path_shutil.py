# -*- coding: utf-8 -*-
import os
import shutil


print('=' * 20)
src = r'data'
dst = r'tmp'
shutil.copytree(src, dst)#
#shutil.move(src, dst)
print('=' * 20)


