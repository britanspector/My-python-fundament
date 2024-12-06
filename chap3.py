# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:06:38 2024

@author: HP
"""

#第三章随记, list列表和相关操作

#列表List = [1,2,3]/['a','b','c']
names = ['messi','neymar','suarez']
print(names[1])
# x.append('') 末尾添加
names.append('havi')
print(names)
# x.insert(n,'') 指定添加
names.insert(3, 'iniesta')
names.insert(4,'busquets')
print(names)
# del x[] 指定删除
del names[0]
print(names)
# x.pop 末尾弹出
lastname = names.pop()
print(lastname)
print(names)
# x.remove()根据值删除元素，只删除列表的第1个出现的该元素
names.remove('busquets')
print(names)
# x.sort()永久对列表排序，首字母顺序
nums = [7,4,8,6,3]
nums.sort()
print(nums)
names.sort()
print(names)
# x.sort(reverse = True)来反方向排列
names.sort(reverse=True)
print(names)
# sorted(x)临时排序并使用  *也可以使用reverse=True
print(sorted(names))
# x.reverse()反转排序，注意！不是按照首字母顺序反转，是按照list本身的排列顺序反转
print(names.reverse())
# len()获取列表长度
print(len(names))
# 关于索引，获取不存在的元素会引发错误，获取-1得到list最后一个元素

