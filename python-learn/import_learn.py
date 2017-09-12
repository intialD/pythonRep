# 学习import和from 。。。import xxx,yyy,...
import sys
from sys import argv, path

print('========================');
print('命令行参数：');

for i in argv :
    print(i);

print('\n python 的路径为：', path);