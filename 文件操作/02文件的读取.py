# _*_ coding : utf-8 _*_
# @Time: 2022/5/20 21:51
# @Author : 程骞
# @File : 02文件的读取
# @Project : python_code

# fp = open("test.txt", "w")
# fp.write("hello world\n" * 5)

# 此时"w"的写入,会覆盖文件内容
# 用"a"可以追加文件内容

# fp1 = open("test.txt", "a")
# fp1.write("hello world\n" *5)

# 文件的读取操作 不能同时写入同时读取

fp2 = open("test.txt", "r")
# content = fp2.read()
# print(content)

# 以上是逐字读取,可以使用readline一行读取(只读取第一行),或者使用readlines多汗读取
# content = fp2.readline()
# readlines读取结果是一个列表,每行都是一项
content = fp2.readlines()
print(content)
