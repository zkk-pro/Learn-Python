# python 变量
# python 的值类型数据有：
# string: 字符串
# number: 数值（整数、浮点数）
# boolean: 布尔值（True、False）

str = "abc"
num = 123
float = 4.56
bool = True


# string
# 字符串可以使用单引号或者双引号，还有三引号（''' ''', 按格式输出）
str2 = '''
你好：
  我是xxx
'''
print(str2)

# 获取字符串的长度
print(len(str2)) # 13(因为有空格格式)

# 获取字符串中的某个字符
print(str[0]) # a
print(str[-1]) # c 获取最后一个字符
# 字符串剪切 语法：str[begin:end] 
print(str[0:2]) # ab
print(str[0:]) # abc 省略 end 表示到最后
print(str[:2]) # ab 省略 begin 表示开始位置（0）
print(str[:]) # abc

# 格式化
first = "create"
last = "404"
full = f"{first} {last}" 
print(full) # create 404
# {} 之间可以放任意表达式
full = f"{first} {len(first)}" # create 6
print(full)

# string 的一些方法
# 转为大写
print(str.upper()) # ABC
# 转为小写
print(str.lower()) # abc
# 首字母转为大写（每一个字母的首字母）
print(str.title()) # Abc
# 删除开头和结尾的空格
print(str.strip()) # abc
print(str.lstrip()) # 删除开头（左侧）空格
print(str.rstrip()) # 删除结尾（右侧）空格
# 获取给定字符串的索引
print(str.find("b")) # 1，返回索引，没有找到返回-1
# 替换字符串
print(str.replace('b', "k")) # akc 返回替换后的字符串
# 是否含有某个字符串
print("b" in str) # True
# 判断某个字符串不属于该字符串
print("z" not in str) # True
# 总结：
# 以上方法都是放回一个新字符串，并不会改变原字符串