# 抛出异常

def calculate(age):
    if age <= 0:
        raise ValueError("年龄不能为0或小于0")
    return 10 / age

# calculate(0)
# 结果
# Traceback (most recent call last):
#   File "/Python/CH6_exceptions/5.raising_exception.py", line 8, in <module>
#     calculate(0)
#   File "/Python/CH6_exceptions/5.raising_exception.py", line 5, in calculate
#     raise ValueError("年龄不能为0或小于0")
# ValueError: 年龄不能为0或小于0

try:
    calculate(0)
except ValueError as err:
    print(err) # 年龄不能为0或小于0

# 总结：
    # 抛出异常时非常消耗资源的行为，so，我们不应该手工抛出异常

