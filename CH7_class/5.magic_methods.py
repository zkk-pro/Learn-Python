# 魔法方法
class Point:
    # __init__ 魔法方法会在创建对象的时候调用
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 直接打印对象 和 把对象转为字符串时调用该方法
    def __str__(self):
        return f"{self.x},{self.y}"
    # 对象的 == 比较
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    # 对象的 > 比较
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    # 通过 __add__ 方法实现 + 操作
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
point = Point(1, 2)
print(point) # 1,2
print(str(point)) # 1,2

# 对象的 == 比较
other = Point(1, 2)
# 默认情况下 对象的 == 比较的是内存地址，重写__eq__方法的比较逻辑
print(point == other) # True

# 对象的 > 比较，通过重写 __gt__ 魔法方法
print(point > other) # False
# 当实现了 __gt__ 方法，就不许要实现 __lt__ (<)方法了
# 解释器会根据 __gt__ 规则自动知道该如何处理 < 号
print(point < other) # False

# 运算符操作 + - * /
# 通过 __add__ 方法实现 + 操作，返回一个新的 Point 实例
conbind = point + other
print(conbind.x)