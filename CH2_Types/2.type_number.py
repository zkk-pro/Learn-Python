# Python 用三种数字类型，分别是：
# 1、整数
# 2、浮点数
# 3、复数（表达式：a + bi，其中i是虚部），在 Python 中，虚部用 j 表示
num1 = 1 # 整数
num2 = 1.2 # 浮点数
num3 = 1 + 2j # 复数

# 数字的运算
print(10 + 3) # 13
print(10 - 3) # 7
print(10 * 3) # 30
print(10 / 3) # 3.3333333333333335 一个 / 得到结果是浮点数
print(10 // 3) # 3 两个 / 得到的结果是整数
print(10 % 3) # 1 取余运算
print(10 ** 3) # 1000 乘方运算

# 数字的常用方法
# 四舍五入
print(round(2.9)) # 3
# 绝对值
print(abs(-2.9)) # 2.9

# 对于更多的代数方法，需要导入 math 模块
# 具体内容查看 math 模块的 文档【中文】https://docs.python.org/zh-cn/3/library/math.html
import math
# 向上取整
print(math.ceil(2.2)) # 3
