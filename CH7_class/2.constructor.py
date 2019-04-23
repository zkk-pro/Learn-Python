# 构造函数
class Point:
    # 构造函数 【self 为指向实例的引用】
    def __init__(self, x, y):
        self.x = x # 表示给实例添加一个x 属性，值为创建实例时传递进来的值
        self.y = y # 所以可以在类的任何方法里都可访问到该属性
    def draw(self):
        print(f"x: {self.x} y: {self.y}")

point = Point(1, 2)
print(point.x) # 1
print(point.y) # 2
point.draw() # x: 1 y: 2