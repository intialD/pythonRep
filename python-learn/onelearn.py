# learn langurage
import sys;

print("hello world");

if True:
    print('Hello, true');
    print("haha");
else:
    print('Hello, false');
# 多行语句
itemOne = 1;
itemTwo = 2;
itemThree = 3;
total = itemOne + \
        itemTwo + \
        itemThree
print(total);

# [],{},()中的多行语句不需要使用 \
hello = [
    'item_one','item_two',
    'item_three',
    'item_four'
]
print(hello);

pargraph = """这是个多行段落，
哈哈哈
"""
print(pargraph);

input('\n\n按下enter键退出');

x = 'runner';
sys.stdout.write(x + '\n');

a = 4
if a > 3 :
    print('hehe');
    print('woca');
elif a < 1 :
    print('ddff');
else :
    print('1<= a <= 3');