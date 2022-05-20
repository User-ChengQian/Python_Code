# _*_ coding : utf-8 _*_
# @Time: 2022/5/19 20:55
# @Author : 程骞
# @File : 08运算符
# @Project : python_code

a = 4
b = 2
c = 8.2
d = 9
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print("-------------")
print(c/a)
print(c//a) # 取整除数
print("-------------")
# 取余
print(d%a)
print("-------------")
# 指数a的b次方
print(a**b)
print("-------------")
# 括号优先级
print((a+b)*b)
# 字符串的拼接
a = "123"
b = "456"
print(a+b)
#特别的,在python中字符串不能与int相加,直接报错
print("-------------")
# 字符串的乘法是重复字符串次数
a = "哇哈哈"
print(a*5)