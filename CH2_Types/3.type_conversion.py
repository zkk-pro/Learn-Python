# 类型转换，有：
# int() 转为整数
# float() 转为浮点数
# bool() 转为布尔值
# str() 转为字符串

# type() 该方法返回对象的类型

# bool() 转换准则 Falsy(类假值) Trusy(类真值)
# Falsy: "", 0 None 这三个值在编译时会被转为 False，其他会转为 True

x = input("输入数字：") # input 方法接收用户的输入，参数传递的是提示
# y = x + 1 # 错误，input 接收到输入的值是 string 类型，相当于："1" + 1
print(type(x)) # <class 'str'>
# 使用类型转换
y = int(x) + 1 # 例如输入的是 1 
print(y) # 2
