# === 第2课：条件判断 if/else ===
# 让程序学会"做选择"，就像人一样根据情况做不同的事

# 1. 最简单的 if
age = 18

if age >= 18:
    print("你是成年人")  # 注意这行前面有4个空格（缩进），表示属于 if 的内容

# 2. if/else —— 二选一
score = 75

if score >= 60:
    print("及格了！")
else:
    print("不及格，继续努力")

# 3. if/elif/else —— 多选一（elif = else if 的缩写）
score = 85

if score >= 90:
    print("优秀！A")
elif score >= 80:
    print("良好！B")
elif score >= 60:
    print("及格！C")
else:
    print("不及格！D")

# 4. 比较运算符
a = 10
b = 20
print(f"a={a}, b={b}")
print(f"a == b ? {a == b}")   # 等于（注意是两个等号）
print(f"a != b ? {a != b}")   # 不等于
print(f"a > b  ? {a > b}")    # 大于
print(f"a < b  ? {a < b}")    # 小于
print(f"a >= b ? {a >= b}")   # 大于等于
print(f"a <= b ? {a <= b}")   # 小于等于

# 5. 逻辑运算符 —— 组合多个条件
age = 25
has_id = True  # True 表示"是"，False 表示"否"

if age >= 18 and has_id:          # and: 两个条件都满足
    print("可以进入酒吧")

if age < 18 or has_id == False:   # or: 至少一个条件满足
    print("不能进入酒吧")

if not (age < 18):                # not: 取反，把 True 变 False
    print("你不是未成年人")

# 6. 实战小例子：简易计算器
num1 = 10
num2 = 3
operator = "+"

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("错误：不能除以0！")
else:
    print(f"不认识的运算符：{operator}")

# === 练习 ===
# 修改下面的变量，看看不同温度会输出什么
temperature = 25

if temperature >= 35:
    print("太热了，开空调！")
elif temperature >= 25:
    print("天气不错，出去走走")
elif temperature >= 10:
    print("有点凉，穿件外套")
else:
    print("太冷了，在家待着吧")
