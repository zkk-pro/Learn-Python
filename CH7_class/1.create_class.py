# 类
# 在 Python 中，类中的方法【至少】有一个参数，
# 第一个参数【默认】是【指向该类实例的引用】，习惯上命名为 self
# 在调用的时候，self 不需要传递实参，Python 内部帮忙处理了

# 定义一个类
class Point:
    def draw(self):
        print("draw...")

# 实例化（使用类创建一个对象）
point = Point()
# 调用类方法
point.draw() # draw...

# 打印类 获取到的是 类型
print(Point)  # <class '__main__.Point'>
# 变量内存地址
print(point) # <__main__.Point object at 0x1007054a8>
# 变量的类型
print(type(point)) # <class '__main__.Point'>
# 判断一个对象是否属于某个类
print(isinstance(point, Point)) # True
