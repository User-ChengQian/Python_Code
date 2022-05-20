# _*_ coding : utf-8 _*_
# @Time: 2022/5/20 19:40
# @Author : 程骞
# @File : 19append,insert,extend方法
# @Project : python_code

list = ["1", "2", "3"]
list.append("1")
print(list)

list = ["1", "2", "3"]
list.insert(1, "插入到第二个")
print(list)

list = ["1" , "2" , "3"]
list2 = ["4", "5"]
list.extend(list2)
print(list)
