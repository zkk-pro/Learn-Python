# 文件读取操作

# file: 文件路径；
# mode: 模式；r：只读，rb：二进制读取（硬盘怎么存就怎么拿）
# encoding: 编码，python3默认为utf-8
# f = open(file="abc.txt", mode="r", encoding="utf-8")
f = open(file="abc.txt", mode="rb")  # 二进制模式不需要 encoding 参数
data = f.read()
print(data)
f.close()

# 只能检测编码工具 chardet
# chardet 是第三方工具，需要安装
# 使用方式：
# import chardet
# result = chardet.detect(open("abc.txt", "rb").read())
