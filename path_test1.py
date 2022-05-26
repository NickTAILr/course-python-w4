# -*- coding: utf-8 -*-
import os

print(os.path.abspath('../'))

# f_obj = open('f.txt', 'w')
# f_obj.write('abcdefg\n')
# f_obj.write('hello world')
# f_obj.close()

# f_obj = open('f.txt', 'r')
# content = f_obj.read()
# # content = f_obj.readline()
# # content = f_obj.readlines()
# f_obj.close()
# print(content)

if not os.path.exists('./data'):
    os.mkdir('./data')

with open('./data/f.txt', 'w') as f_obj:
    f_obj.write('hello world')

print(os.path.basename('./data/f.txt'))
