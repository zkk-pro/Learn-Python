# 逻辑运算符
# and 与
# or 或
# not 非

age = 22
country = "zh"
gander = "girl"

if age >= 18 and country == "zh":
    print("It's OK")
else:
    print("not OK")

# 更复杂的运算：年龄大于18 或者 是中国国籍的 并且 性别不是女的
if (age >= 18 or country == "zh") and not gander:
  print("OK")
else:
  print("not OK")