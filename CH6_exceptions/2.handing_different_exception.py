# 处理不同的异常
try:
    age = int(input("输入你的年龄："))
    divisor = 10 / age # 被除数为 0
except ValueError:
    print("年龄必须为数字")
except ZeroDivisionError:
    print("年龄不能为0")
else:
    print("没有异常")

# 另一种处理方式：多个异常提示相同错误提示
try:
    age = int(input("输入你的年龄："))
    divisor = 10 / age # 被除数为 0
except (ValueError, ZeroDivisionError):
    print("年龄不合法")
else:
    print("没有异常")

# 总结：
#     多条异常处理时，只要程序执行到了一条异常，后面的异常语句就不被执行