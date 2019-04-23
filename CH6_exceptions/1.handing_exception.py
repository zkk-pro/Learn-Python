# 处理异常
l = [1, 2]
# l[2] # 访问不存在的索引
# 报错
# Traceback (most recent call last):
#   File "/Python/CH6_exceptions/1.handing_exception.py", line 3, in <module>
#     l[2]
# IndexError: list index out of range

# 处理异常
try:
    l[2] # 访问不存在的索引
except IndexError:
    print("访问了不在的索引")

# try...except...else 语句：当没有发生异常时，最后会执行 else 语句
try:
    l[1] # 存在的索引
except IndexError:
    print("访问了不在的索引")
else:
    print("程序没有发生异常")

# 获取具体异常信息 和 异常类型
try:
    l[2] # 不存在的索引
except IndexError as ex:
    print("访问了不在的索引")
    print("异常是：", ex) # 异常是： list index out of range
    print("异常类型：", type(ex)) # 异常类型： <class 'IndexError'>
else:
    print("程序没有发生异常")