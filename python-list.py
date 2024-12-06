#第四章  操作列表list

#循环遍历列表
families = ['mom','dad', 'me']  #整个列表
for family in families:     #定义新变量为列表里每个元素，并分别操作
    print(family)

#尝试操作数字列表，依次读取并操作每个元素
nums = [3,5,7,8]
for num in nums:
    print(num**2)

#进一步操作
for family in families:
    print(f"{family.title()} is a member of our family.")

#使用for时记得检查缩进！检查冒号：！

#使用range(开头，不存在的结尾，步长) 来生成一组整数，注意有头无尾。1-5只包含1，2，3，4.
#使用list（）来把生成的这组数转成列表
nums1 = list(range(1,8,2))
print(nums1)

#直接操作每个数
aSquare = []  #初始化列表来存
for a in range(1,10,2):
    aSquare.append(a**2)
print(aSquare)

#一些列表统计运算
print(min(aSquare))
print(max(aSquare))
print(sum(aSquare))

#列表解析，更快速但较复杂的--处理一组数据+构成列表
mylist = [number**2 for number in range(1,13,2)]
print(mylist)

#列表切片
print(mylist[1:4])  #将使用列表的1,2,3号元素，通俗来讲的第2，3，4个元素（因为第1个元素是0号元素）
print(mylist[:2])   #从头开始
print(mylist[4:])   #直到结束
print(mylist[-2:])  #最后n个

#遍历切片
for number in mylist[1:3]:
    print(number+1)

#复制列表：区分切片复制（只复制了元素到另一个地址不同的列表） & 直接赋值(等于直接地址相同，两个列表时刻同步)
copylist1 = mylist[:]  #切片
copylist2 = mylist   #直接
mylist.append(1000)
copylist1.append(0)   #分别操作一下
copylist2.append(100)
print(copylist1,copylist2)

#元组，不可修改的“列表”。（除非重新定义）