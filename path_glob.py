# -*- coding: utf-8 -*-
import os
import glob


print('=' * 20)
file_name = 'RT0/1/NO4. RT-15-1.bmp'
print(f'file_name = {file_name}')
print('=' * 20)

a = os.path.dirname(file_name)
b = os.path.basename(file_name)
c = os.path.split(file_name)
d = os.path.splitext(file_name)
print(f'os.path.dirname() = {a}')
print(f'os.path.basename() = {b}')
print(f'os.path.split() = {c}')
print(f'os.path.splitext() = {d}')
print('=' * 20)

data_dir = os.getcwd()
gt_file_list = glob.glob(os.path.join(data_dir, "*.py"))#取所有.py檔案的路徑

for root, dirs, files in os.walk(data_dir):
    print(f'root = {root}')
    print(f'dirs = {dirs}')
    print(f'files = {files}')
print('=' * 20)

os.mkdir(os.path.basename(os.path.dirname(file_name)))
os.makedirs(os.path.dirname(file_name))
print('=' * 20)


temp_path = "tmp"
if not os.path.exists(temp_path):#不存在則創建檔案，存在則略過
    os.mkdir(temp_path)#無法創造多層，中間層目錄不存在會抱錯
#可使用makedirs 例:os.makedirs('test1/ts/ttt')
retval = os.getcwd()
print(f'當前工作目錄為 {retval}')
os.chdir(temp_path)
retval = os.getcwd()
print(f'目錄修改成功 {retval}')
print('=' * 20)

