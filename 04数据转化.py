# _*_ coding : utf-8 _*_
# @Time: 2022/5/19 20:12
# @Author : 程骞
# @File : 04数据转化
# @Project : python_code

# '1.23'和'1ab'这类字符串不能转为int类型,会报错
a = '123'
print(type(a))
b = int(a)
print(type(b))

a = 1.99
b = int(a)
print(b) # 不会四舍五入

a = True # true代表1  false代表0
b = int(a)
print(b)

