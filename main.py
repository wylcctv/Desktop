# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from _typeshed import IdentityFunction
import os
import myMoudle_demo



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


raw = r"Newlines are indicated by \n"

runningList = []


# while循环方法
def while_():
    print(raw)
    number = 11
    running = True
    print('----------进入while关卡-------')
    while running:
        guess = int(input('请输入一个数值：'))
        runningList.append(guess)
        if number == guess:
            print('恭喜你，猜对了！')
            running = False
        elif guess < number and guess != 0:
            print('你输入的值比结果小！')
        elif guess > number and guess != 0:
            print('你输入的值比结果大')
        elif guess == 0:
            print('输入0，退出程序,，输入的结果为{0}，输入的次数为{1}'.format(runningList, len(runningList)))
            running = False


# for循环方法
def for_():
    print('----------进入for关卡-------')
    for i in range(1, len(runningList), 2):
        print('当前循环是：', i)


# 方法中的可变参数
def total(a=5, *numbers, **phonebook):
    print('a', a)
    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


# 数组、元组、集合
def object_(a):
    # List 操作
    if a == 1:
        shoplist = ['apple', 'mango', 'carrot', 'banana']
        print('我有', len(shoplist), '的东西要买！')
        print('这些是：', end=' ')
        for item in shoplist:
            print(item, end=' ')

        print('\n我还要买大米')
        shoplist.append('rice')
        print('my shoping list is now:', shoplist)

        print('我现在整理我的名单，i will sort my list now')
        shoplist.sort()
        print('分类清单为：', shoplist)

        print('我要看的第一件事情是：the fiest item I will buy is ', shoplist[0])
        olditm = shoplist[0]
        del shoplist[0]
        print('我买了那辆车:', olditm)
        print('分类清单现在为：', shoplist)
    if a == 2:
        zoo = ('python', 'elephant', 'penguin')
        print('如果动物园动物的数量是：', zoo)




input_ = int(input('请输入你想使用的工具 \n '
                   '1: 运行while循环 \n '
                   '2: 运行for循环 \n'
                   '3: 运行方法中可变参数测试小功能 \n    '
                   '4: 测试模块代码方法 \n'
                   '5: 面向对象,list-1 元组-2 集合-3 \n'
                   )
             )
if input_ == 1:
    while_()
elif input_ == 2:
    for_()
elif input_ == 3:
    print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
elif input_ == 4:
    myMoudle_demo.say_hi()
    print(myMoudle_demo.__version__)
elif input_ == 5:
    object_(1)

print('----------------------------------')
print(dir(myMoudle_demo))
