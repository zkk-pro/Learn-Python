# 条件语句声明 和 三元运算符
# PEP8 建议的缩进是4个空格

# 条件语句
temperature = 35
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# 三元运算
age = 12
info = "ok" if age >= 18 else "no ok"
print(info)