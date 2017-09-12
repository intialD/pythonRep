a,b,c,d = 1, 5.5, True, 4+3j;
print(type(a), type(b), type(c), type(d));
print(isinstance(a, int));

## isinstance 和type的区别
class A:
    pass

class B(A):
    pass

print(isinstance(A(), A));
print(type(A()) == A);
# isinstance 会认为子类是一种父类类型
print(isinstance(B(), A));
# type不会认为子类是一种父类类型
print(type(B()) == A);

print(type(A));

print('==============================')
str = 'Runoob';
print(str);
print(str[0:-1]);# 输出第一个字符串到倒数第二个的所有字符串
print(str[0]); # 输出字符串的第一个字符
print(str[2:5]);# 输出从第三个到第五个的字符
print(str[2:]); # 输出从第三个开始后的所有字符
print(str * 2); # 输出字符串两次
print(str + 'TEST'); # 连接字符串
