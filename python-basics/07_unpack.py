# === 第7课：解包语法 ** ===
# 学完这课，agent_loop 代码你就 100% 看懂了

# ============ 第一部分：从一个实际问题说起 ============

# 1. 假设你有一个函数
def make_card(name, age, job):
    print(f"【名片】{name} | {age}岁 | {job}")

# 正常调用：一个个传参数
make_card("小白", 25, "产品经理")

print("---")

# 2. 但如果参数已经存在于一个字典里呢？
info = {"name": "小白", "age": 25, "job": "产品经理"}

# 笨办法：一个个取出来传
make_card(info["name"], info["age"], info["job"])

# 聪明办法：用 ** 一次性"解包"
make_card(**info)  # 等价于 make_card(name="小白", age=25, job="产品经理")

# 三种写法，效果完全一样！

print("---")

# ============ 第二部分：** 到底做了什么？ ============

# 3. ** 就是"把字典拆开，变成 key=value 的形式"
#
# 原始字典：{"name": "小白", "age": 25, "job": "产品经理"}
#
# **字典 → name="小白", age=25, job="产品经理"
#
# 就像拆快递：
#   📦 {"name": "小白", "age": 25}  ← 打包的字典
#   ** 拆开 →  name="小白", age=25   ← 拆成一个个参数

# 4. 再看几个例子
def greet(greeting, name):
    print(f"{greeting}, {name}!")

params = {"greeting": "你好", "name": "小白"}
greet(**params)  # 等价于 greet(greeting="你好", name="小白")

print("---")

# 5. 字典的 key 必须和函数参数名对得上
def add(a, b):
    return a + b

numbers = {"a": 10, "b": 20}
result = add(**numbers)  # 等价于 add(a=10, b=20)
print(f"10 + 20 = {result}")

# 如果 key 对不上会报错：
# wrong = {"x": 10, "y": 20}
# add(**wrong)  # 报错！函数要的是 a 和 b，不是 x 和 y

print("---")

# ============ 第三部分：回看 agent_loop ============

# 6. 模拟 agent_loop 中的工具调用

# 这是"工具函数表"——每个工具名对应一个函数
def get_weather(city):
    return f"{city}：32°C 晴"

def search(query, limit=3):
    return f"搜索「{query}」，返回前{limit}条结果"

TOOL_HANDLERS = {
    "get_weather": get_weather,
    "search": search,
}

# 模拟 Claude 返回的工具调用请求
class ToolBlock:
    def __init__(self, name, input_data):
        self.name = name      # 工具名
        self.input = input_data  # 参数（字典）

# Claude 说："我要用 get_weather 工具，参数是 city=北京"
block = ToolBlock("get_weather", {"city": "北京"})

# 代码怎么执行的：
print("一步步拆解：")
print(f"  block.name  = {block.name}")       # "get_weather"
print(f"  block.input = {block.input}")      # {"city": "北京"}

# TOOL_HANDLERS[block.name] → TOOL_HANDLERS["get_weather"] → get_weather 函数
handler = TOOL_HANDLERS[block.name]
print(f"  找到函数    = {handler.__name__}")

# **block.input → **{"city": "北京"} → city="北京"
output = handler(**block.input)  # 等价于 get_weather(city="北京")
print(f"  执行结果    = {output}")

print("---")

# 再试一个：搜索工具
block2 = ToolBlock("search", {"query": "Python教程", "limit": 5})
handler2 = TOOL_HANDLERS[block2.name]
output2 = handler2(**block2.input)  # 等价于 search(query="Python教程", limit=5)
print(f"搜索结果：{output2}")

print("---")

# ============ 第四部分：完整翻译 ============

print("=== agent_loop 第16-17行完整翻译 ===")
print()
print("代码：output = TOOL_HANDLERS[block.name](**block.input)")
print()
print("拆解：")
print("  TOOL_HANDLERS[block.name]  → 根据工具名，找到对应的函数")
print("  **block.input              → 把参数字典拆开")
print("  函数(**参数)               → 调用函数")
print("  output =                   → 把结果存起来")
print()
print("翻译成人话：")
print("  \"根据 Claude 说的工具名，找到对应的函数，")
print("   把 Claude 给的参数传进去执行，拿到结果\"")

print()
print("🎉 恭喜！agent_loop 的每一行你都能看懂了！")
