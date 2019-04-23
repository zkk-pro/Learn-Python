# with 语句
# with 关键字 为一些操作对象 自动释放资源，但不是任何操作都可以，只针对一些特定
# 的对象管用，那么如何判定哪些对象可用呢？下面再讲解

try:
    with open("1.handing_exception.py") as fs:
    # 操作多个文件
    # with open("1.handing_exception.py") as fs, open("3.cleaning_up.py") as fs
        print("文件已打开")
        print(fs)

        # 判断对象是否可用 with 关键字结合，当对象有下面两个方法时，就代表可用，
        # 称为对象支持 “上下文管理协议”
        # 结合 with 语句，python 会自动调用__exit__方法来释放资源，操作多个资源也是。
        # fs.__enter__
        # fs.__exit__


    # 一些代码，可能发生异常
    age = int(input("输入你的年龄："))
    divisor = 10 / age # 被除数为 0
    # fs.close() # 上面可能代码可能发生异常，那么这句话就不执行
except (ValueError, ZeroDivisionError):
    print("年龄不合法")
    # fs.close() # 放在这也不行，如果没异常，这里不执行