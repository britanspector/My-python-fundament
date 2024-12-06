# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:54:41 2024

@author: HP
"""
#第二章练习

#case 2-3 & 2-4
name = 'messi'
ask = f"Hello {name.title()}, would you like to play soccer today?"
print(ask)

#case 2-5 & 2-6
message = '"I love soccer."'
print(f"{name.title()} once said, {message}")

#case 2-7
name1 = 'van dijk\n'
name2 = 'van dijk\t'
print(name1,'\n',name2)  #新发现！如果用print打印两个变量，会自动存在一个空格来分割两个变量！
print(name1.rstrip(),'\n',name2.rstrip())
