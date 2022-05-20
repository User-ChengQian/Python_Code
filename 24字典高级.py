# _*_ coding : utf-8 _*_
# @Time: 2022/5/20 20:33
# @Author : 程骞
# @File : 24字典高级
# @Project : python_code

a_dist={"name":"zs" , "age":19}
print(a_dist)


# 访问成员
print(a_dist["name"])
# 若访问的成员不存在,会报错

# 访问成员2
# 方法2获取不存在的成员输出none
print(a_dist.get("name"))
print(a_dist.get('sex'))

# 字典的修改(无set修改的方法)
a_dist["name"]="ls"
print(a_dist)

# 字典的增加(增加不存在的值)
a_dist["sex"]="boy"
print(a_dist)
print("-----------")
# 字典的删除
# 1.del
# 2.clear
a_dist={"name":"zs","age":18}
# del删除指定的成员
del a_dist["name"]
print(a_dist)
# del删除本字典(不能再次输出)
# del a_dist

# clear清空字典(仍然保留字典)
a_dist.clear()
print(a_dist)

