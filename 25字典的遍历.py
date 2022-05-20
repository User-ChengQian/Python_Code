# _*_ coding : utf-8 _*_
# @Time: 2022/5/20 20:56
# @Author : 程骞
# @File : 25字典的遍历
# @Project : python_code


a_dist = {"name":"zs", "age":18}

# 1.遍历key值,使用字典.keys()方法
for key in a_dist.keys():
    print(key)
# 2.遍历value,使用字典.value()方法
for value in a_dist.values():
    print(value)
print("--------------")
# 3.遍历key和value,使用字典.items()方法
for key,value in a_dist.items():
    print(key,value)
    print("--------------")
# 4.遍历每一个item项(类似元组格式),使用字典.items()方法
for item in a_dist.items():
    print(item)