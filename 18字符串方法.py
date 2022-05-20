# _*_ coding : utf-8 _*_
# @Time: 2022/5/20 15:30
# @Author : 程骞
# @File : 18字符串方法
# @Project : python_code

# 1len获取长度
# 2find查找内容  返回第一个索引
# 3startswith,endswith 判断字符串不是以某字符开头或结尾
# 4count 统计字符次数
# 5replace 替换字符串中的内容
# 6split  通过参数的内容切割字符串
# 7upper,lower 将字符串中的大小写互换
# 8strip 去空格
# 9join 字符串拼接


a = "today520"
print(len(a))
print(a.find("a"))
print(a.startswith("t"))
print(a.endswith("2"))
print(a.count("t"))
print(a.split("5"))
print(a.upper())
b = "   a    "
c = "#"
print(b.strip())
print(c.join(a))