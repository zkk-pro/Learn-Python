# 清理工作（释放资源）
# 例如打开一个文件，操作完后一定要关闭，不然别的程序就无法访问

try:
    fs = open("1.handing_exception.py")
    print(fs)
    # 一些代码，可能发生异常
    age = int(input("输入你的年龄："))
    divisor = 10 / age # 被除数为 0
    # fs.close() # 上面可能代码可能发生异常，那么这句话就不执行
except (ValueError, ZeroDivisionError):
    print("年龄不合法")
    # fs.close() # 放在这也不行，如果没异常，这里不执行
finally:
    fs.close() 