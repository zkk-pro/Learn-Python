# 自定义容器（类型）
class TagCloud:
    def __init__(self):
        self.tags = {}
    
    def add(self, tag):
        # dict提供的get()方法，
        # 如果key不存在，可以返回None，或者自己指定的value：
        # 如果key存在，返回key 对应的值
        # self.tags[tag] = self.tags.get(tag, 0) + 1
        # 把参数都转为小写，解决大小敏感问题
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    # 读取值
    def __getitem__(self, tag):
        # 返回指定 tag 的值，没有就返回 0
        return self.tags.get(tag.lower(), 0)
    # 设置值
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    # 查看长度
    def __len__(self):
        return len(self.tags)
    # 使对象可迭代
    def __iter__(self):
        # 使用内建函数获得一个迭代器
        # 迭代器是一个容器，每次读取迭代的一个值
        return iter(self.tags)
    
cloud = TagCloud()
cloud.add('python')
cloud.add('python')
cloud.add('python')
print(cloud.tags) # {'python': 3}

# 为什么有了字典，还需要自定义类
# 例如：在添加 tag 时，Python 和 python 应该是同一个的
# 但实际是
cloud.add('Python')
print(cloud.tags) # {'python': 3, 'Python': 1}
# 所以，可以在 add 方法里把参数都转为小写，解决大小敏感问题

# 读取值
print(cloud['python']) # 4
print(cloud['Python']) # 4

# 设置值
cloud['js'] = 10
print(cloud.tags) # {'python': 4, 'js': 10}

# 查看长度
print(len(cloud)) # 2

# 迭代对象
for key in cloud:
    print(key)
# 结果：
# python
# js