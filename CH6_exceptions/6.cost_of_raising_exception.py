
'''
抛出异常的消耗
    抛出异常是很消耗性能的，测试一下抛出异常的消耗对比另一种处理异常的消耗，接近4倍
'''

from timeit import timeit

code1 = '''
def calculate(age):
    if age <= 0:
        raise ValueError("年龄不能为0或小于0")
    return 10 / age

try:
    calculate(0)
except ValueError as err:
    # print(err) # 年龄不能为0或小于0
    pass
'''

code2 = '''
def calculate(age):
    if age <= 0:
        return None
    return 10 / age

res = calculate(0)
if res == None:
    pass
'''

# 参数1：字符串代码；参数2：执行次数
print(timeit(code1, number=10000)) 
# 结果
# 使用print 打印异常信息：0.24884426499999998
# 使用pass 0.004616803999999999

print(timeit(code2, number=10000)) # 001676432999999998