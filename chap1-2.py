# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:32:30 2024

@author: HP
"""
#第二章的随记

#关于format的使用方法，以及title（）、upper（）和lower（）函数
hello_1 = 'hello world'
hello_2 = ' for you'
hello_3 = f"{hello_1}{hello_2}"
print(hello_3)
print(hello_3.title())
print(hello_3.lower())
print(hello_3.upper())

#制表符\t 换行符\n
print("lionel\tmessi")
print("lionel\nmessi")

#删除空白 rstrip() & lstrip() & strip()
#暂时删除
print(hello_2.lstrip())
print(hello_2)
#永久删除
hello_2d = hello_2.lstrip()
print(hello_2d)

#Attention! Don't use ' between '', will cause wrong!!!

#小数运算结尾位数可能不确定！
print(0.2+0.1)

#两数相除一定是浮点数哦！并且运算涉及float结果一定是float
print(4/2) #看吧，是2.0不是2

#写大数可以用下划线分割，但打印出来没有_
bignum = 14_000_000
print(bignum)

#多变量赋值：
x,y,z = 1,2,3
print(x,y,z)

#常量
GOAT = 'L.Messi'
print(GOAT)

#python之禅
import this