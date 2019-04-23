# 类属性 和 实例属性
class Point:
    # 类属性（被所有实例对象共享）
    default_color = "red"

    # 构造函数 【self 为指向实例的引用】
    def __init__(self, x, y):
        self.x = x # 表示给实例添加一个x 属性，值为创建实例时传递进来的值
        self.y = y # 所以可以在类的任何方法里都可访问到该属性
    def draw(self):
        print(f"x: {self.x} y: {self.y}")

# 在实例化的时候指定一些属性
point = Point(1, 2)
# 也可以在创建对象之后添加属性，因为 Python 的对象是动态的
point.z = 10

# 现在 point 有 x,y,z 属性，换句话说
# 这些属性都属于 point 实例对象

# 类的属性 在所有实例中是共享的
# 通过实例访问 类的属性
print(point.default_color) # red
# 通过类访问 类的属性
print(Point.default_color) # red