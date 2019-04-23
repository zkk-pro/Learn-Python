# 找出出现最多的字符

chars = "Every generation has a legend. Watch the brand-new teaser for Star Wars: Episode IX."

# 转为 dict 并记录次数
char_dict = {}
for char in chars:
  if (char in char_dict):
    char_dict[char] += 1
  else:
    char_dict[char] = 1

print(char_dict)
# 结果：
# {'E': 2, 'v': 1, 'e': 10, 'r': 7, 'y': 1, ' ': 13, 
# 'g': 2, 'n': 5, 'a': 8, 't': 5, 'i': 2, 'o': 3, 'h': 3, 
# 's': 4, 'l': 1, 'd': 3, '.': 2, 'W': 2, 'c': 1, 'b': 1, 
# '-': 1, 'w': 1, 'f': 1, 'S': 1, ':': 1, 'p': 1, 'I': 1, 
# 'X': 1}

# print(sorted(char_dict.items()))
# 结果
# [(' ', 13), ('-', 1), ('.', 2), (':', 1), ('E', 2), ('I', 1), 
# ('S', 1), ('W', 2), ('X', 1), ('a', 8), ('b', 1), ('c', 1), 
# ('d', 3), ('e', 10), ('f', 1), ('g', 2), ('h', 3), ('i', 2), 
# ('l', 1), ('n', 5), ('o', 3), ('p', 1), ('r', 7), ('s', 4), 
# ('t', 5), ('v', 1), ('w', 1), ('y', 1)]

# 转为list，list 的每一项为tuple，并排序(倒序)
char_sorted = sorted(char_dict.items(), key=lambda item:item[1], reverse=True)
print(char_sorted[0]) # (' ', 13)

