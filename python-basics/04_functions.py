# === 第4课：函数 ===
# 把代码打包成"工具"，起个名字，随时调用

# 1. 最简单的函数
def say_hello():
    print("你好！")

say_hello()  # 调用函数
say_hello()  # 可以反复调用

print("---")

# 2. 带参数的函数 —— 让工具更灵活
# 参数就是"输入"，告诉函数要处理什么
def greet(name):
    print(f"你好，{name}！")

greet("小白")
greet("小明")
greet("产品经理")

print("---")

# 3. 多个参数
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(3, 5)
add(100, 200)

print("---")

# 4. 返回值 —— 函数把结果"交还"给你
# print 是"说出来"，return 是"交回来"
def multiply(a, b):
    return a * b  # 把结果返回，不是打印

result = multiply(4, 5)  # result 接住返回值
print(f"4 × 5 = {result}")

# 返回值可以继续参与计算
total = multiply(3, 4) + multiply(5, 6)
print(f"3×4 + 5×6 = {total}")

print("---")

# 5. 默认参数 —— 给参数一个"默认值"
def make_coffee(size="中杯", sugar=True):
    sugar_text = "加糖" if sugar else "不加糖"
    print(f"一杯{size}咖啡，{sugar_text}")

make_coffee()                    # 全用默认值
make_coffee("大杯")              # 只改 size
make_coffee("小杯", False)       # 都改
make_coffee(sugar=False)         # 只改 sugar（用参数名指定）

print("---")

# 6. 函数调用函数 —— 像搭积木一样组合
def is_adult(age):
    return age >= 18

def check_entry(name, age):
    if is_adult(age):  # 调用上面的函数
        print(f"{name}，欢迎入场！")
    else:
        print(f"{name}，未成年人不能进入")

check_entry("小白", 25)
check_entry("小明", 15)

print("---")

# 7. 实战：温度转换器
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temp_c = 37
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 100
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")  # :.1f 保留1位小数

print("---")

# 8. 回看 agent_loop —— 现在你能看懂第1行了
# def agent_loop(messages):
#     ↑      ↑        ↑
#   定义   函数名    参数（对话记录列表）
#
# 这就是一个函数！接收 messages 作为输入，
# 里面的代码就是这个函数要做的事

# === 练习 ===
# 写一个函数，输入你的名字和爱好，输出自我介绍
def introduce(name, hobby):
    return f"大家好，我是{name}，我喜欢{hobby}！"

print(introduce("小白", "coding"))
print(introduce("你的名字", "你的爱好"))
