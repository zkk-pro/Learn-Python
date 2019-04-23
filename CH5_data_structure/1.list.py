# 数据结构：list

# 【生成 list 方式】
letters = ['a', 'b', 'c']

# 生成多个相同的元素
zeros = [0] * 10
print(zeros)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 合并 list
combined = letters + zeros
# combined = letters + [1, 2, 3]
print(combined)  # ['a', 'b', 'c', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 快速生成 list: list(),该方法接收一个 可迭代对象，返回一个 list
numbers = list(range(10))
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chars = list("hello world")
print(chars)  # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# 获取 list 的长度（元素个数）
print(len(chars))  # 11


# 【 list 常用操作方法 】
# 访问 list 元素
letters = ['a', 'b', 'c', 'd']
print(letters[0])  # a

# 修改
letters[0] = 'A'
print(letters)  # ['A', 'b', 'c', 'd']

# 切割（都是返回新的字符串）
print(letters[0:3]) # ['A', 'b', 'c']
print(letters[:3]) # ['A', 'b', 'c']
print(letters[:]) # ['A', 'b', 'c', 'd']
# 步进方式
print(letters[::2]) # ['A', 'c']

numbers = list(range(10))
print(numbers[::2]) # [0, 2, 4, 6, 8]
# 倒序的
print(numbers[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# 【 list 拆箱 】
numbers = [1, 2, 3]
# 拆箱操作，注意：左边的熟练必须和 list 元素个数一致，否则报错
first, second, third = numbers
print(first, second, third) # 1 2 3

# 只想要部分数据 （拆箱有装箱）
numbers = [1, 2, 3, 5, 6, 7]
first, second, *other = numbers
print(first, second, other) # 1 2 [3, 5, 6, 7]

# 只想要第一个 和 最后一个
first, *other, last = numbers
print(first, other, last) # 1 [2, 3, 5, 6] 7