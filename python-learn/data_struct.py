# 常用数据结构 List
exeList = [123, '234','hell', 70.2];
tinyList = ['woca', 21];

tinyList[1] = 35;
print(exeList);
print(exeList[0]);
print(exeList[1:3]);
print(exeList[2:]);
print(exeList + tinyList);

# Tuple(元组)，元素不能修改
tuple = ('abc',123,'ccc',70.5);
tinyTuple = ('woca','heiheihei');
print('====================');
print(tuple);
print(tuple[0]);
print(tuple[1:3]);
print(tuple[2:]);
print(tuple * 2);
print(tuple + tinyTuple);

# 集合（set）
print('=============set');
student = {'tome','hello','lily','lucy','lucy'};
print(student);
if ('tome' in student) :
    print('in set student');
else:
    print('not in set student');

a = set('abcaaadefdd');
b = set('mnadb');
print(a);
print(a - b); # a b 差集
print(a | b); # a b 并集
print(a & b); # a b求交集
print(a ^ b); # a b不同时存在的元素
    