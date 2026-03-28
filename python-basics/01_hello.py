# === 第1课：Hello World 和变量 ===

# 1. 打印输出 —— 你的第一行代码
print("Hello, World!")
print("你好，小白！欢迎来到 Python 的世界")

# 2. 变量 —— 给要打印的数据起名字
# 变量就像一个有名字的盒子，你往里面放东西，以后用盒子的名字就能取出来
name = "小白"
age = 25
height = 1.75

print(name)    # 输出: 小白
print(age)     # 输出: 25
print(height)  # 输出: 1.75

# 3. 字符串拼接 —— 用 + 把字符串和变量粘在一起
print("我的名字是 " + name)
print(f"我叫{name}，今年{age}岁")  # f-string，更方便的写法

# 4. 基本数学运算
a = 10
b = 3

print(f"{a} + {b} = {a + b}")   # 加法
print(f"{a} - {b} = {a - b}")   # 减法
print(f"{a} * {b} = {a * b}")   # 乘法
print(f"{a} / {b} = {a / b}")   # 除法（有小数）
print(f"{a} // {b} = {a // b}") # 整除（去掉小数）
print(f"{a} % {b} = {a % b}")   # 取余数
print(f"{a} ** {b} = {a ** b}") # 幂运算（10的3次方）

# === 练习 ===
# 试试修改下面的变量，然后运行这个文件看看效果
my_name = "小白"
my_hobby = "coding"
print(f"大家好，我是{my_name}，我喜欢{my_hobby}！")
