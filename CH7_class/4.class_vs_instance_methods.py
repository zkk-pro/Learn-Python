# 类方法 和 实例方法
# 有时候，需要创建一个复杂对象时，

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 创建类方法
    # 使用装饰器 @classmethod 参数 cls 就会指向【该类】的引用
    @classmethod
    def zero(cls):
        return cls(1, 2) # 相当于 Point(1, 2)

    def draw(self):
        print(f"x: {self.x} y: {self.y}")
# 创建对象的方式 1
point = Point(1, 2)

# 创建对象的方式 2
# zero 是 类方法，调用该方法会返回一个 point 对象
# 这种方式称为工厂函数
point = Point.zero() 
print(point) # <__main__.Point object at 0x1080e50f0>
print(point.x) # 1
point.draw() # x: 1 y: 2
