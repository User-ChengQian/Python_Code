# _*_ coding : utf-8 _*_
# @Time: 2022/5/20 21:39
# @Author : 程骞
# @File : 01文件的读写和关闭
# @Project : python_code

# 文件格式"w"为可读,"r"为可写


fp = open("test.txt", "w")
fp.write("hello world")

# 可以创建文件,但是不可以创建文件夹
fp2 = open("./demo/test.txt", "w")

# 每次打开读写过文件后,需要关闭文件
fp2.close()
