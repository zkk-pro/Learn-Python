# for 循环

for num in range(3):
    print("次数：", num + 1, (num + 1) * ".")
# 次数： 1 .
# 次数： 2 ..
# 次数： 3 ...

# 另一种写法： 指定开始和结束
for num in range(1, 4):
    print("次数：", num, num * ".")
# 次数： 1 .
# 次数： 2 ..
# 次数： 3 ...

# 指定间隔
for num in range(1, 11, 2):
    print("次数：", num, num * ".")
# 次数： 1 .
# 次数： 3 ...
# 次数： 5 .....
# 次数： 7 .......
# 次数： 9 .........

# for...else 语句
# 在【顺利】（for 循环没有被 break）执行完 for 循环后，会执行 else 语句块
# 重复发送短信3次，成功则跳出发送
successful = True
for num in range(3):
    print("发送短信")
    if successful:
        print("发送成功")
        break
else:
    print("发送失败")
# result:
# successful = True
#   发送短信
#   发送成功
# successful = False
    # 发送短信
    # 发送短信
    # 发送短信
    # 发送失败
