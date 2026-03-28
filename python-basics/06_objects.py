# === 第6课：对象和方法 ===
# "点号"到底是什么意思？为什么到处都是 xxx.yyy？

# ============ 第一部分：点号 = "的" ============

# 1. 你其实已经用过点号了
fruits = ["苹果", "香蕉"]
fruits.append("橘子")     # 列表.添加()
# ↑ 读作：fruits 的 append 方法

name = "hello world"
print(name.upper())       # 字符串.转大写()
print(name.replace("world", "小白"))  # 字符串.替换()
print(name.split(" "))    # 字符串.按空格拆分()

print("---")

# 2. 点号的核心含义
# xxx.yyy 就是 "xxx 的 yyy"
# xxx.yyy() 就是 "让 xxx 执行 yyy 这个动作"
#
# 生活类比：
#   手机.打电话()     → phone.call()
#   手机.品牌         → phone.brand
#   冰箱.打开()       → fridge.open()
#   冰箱.温度         → fridge.temperature

# ============ 第二部分：用 class 造自己的对象 ============

# 3. 最简单的 class —— 造一个"人"
class Person:
    def __init__(self, name, age):  # 初始化，创建时自动调用
        self.name = name  # self.name = 这个人的名字
        self.age = age    # self.age = 这个人的年龄

    def introduce(self):  # 方法 = 这个对象能做的事
        print(f"我叫{self.name}，今年{self.age}岁")

    def is_adult(self):
        return self.age >= 18

# 创建对象（实例化）
小白 = Person("小白", 25)
xiaoming = Person("小明", 15)

# 用点号访问属性和方法
print(小白.name)         # 属性：小白 的 name
print(小白.age)          # 属性：小白 的 age
小白.introduce()         # 方法：小白 的 自我介绍()
print(f"成年人？{小白.is_adult()}")

print()
xiaoming.introduce()
print(f"成年人？{xiaoming.is_adult()}")

print("---")

# 4. 链式点号 —— 一层一层往里找
class Phone:
    def __init__(self, brand, owner):
        self.brand = brand
        self.owner = owner  # owner 是一个 Person 对象

my_phone = Phone("iPhone", 小白)

# 链式访问
print(my_phone.brand)              # 手机的品牌
print(my_phone.owner.name)         # 手机的主人的名字
print(my_phone.owner.age)          # 手机的主人的年龄
my_phone.owner.introduce()         # 手机的主人.自我介绍()

print("---")

# ============ 第三部分：带方法返回值的对象 ============

# 5. 方法可以返回另一个对象
class ChatClient:
    def __init__(self, name):
        self.name = name
        self.messages = MessageService()  # 属性本身是另一个对象

    def info(self):
        print(f"客户端：{self.name}")

class MessageService:
    def create(self, model, content):
        # 返回一个 Response 对象
        return Response(
            content=f"[{model}] 回复：已收到「{content}」",
            stop_reason="end_turn",
        )

class Response:
    def __init__(self, content, stop_reason):
        self.content = content
        self.stop_reason = stop_reason

# 使用
client = ChatClient("我的AI助手")
client.info()

# 链式调用：client.messages.create(...)
# 读作：客户端 的 消息服务 的 创建方法
response = client.messages.create(
    model="claude",
    content="你好",
)

print(f"回复内容：{response.content}")
print(f"停止原因：{response.stop_reason}")

# 用点号拿属性来判断
if response.stop_reason != "tool_use":
    print("不需要工具，直接返回答案")

print("---")

# ============ 第四部分：回看 agent_loop ============

# 6. 现在逐行翻译 agent_loop：
print("=== agent_loop 逐行翻译 ===")
print()
print("代码：client.messages.create(model=MODEL, ...)")
print("翻译：客户端 的 消息服务 的 创建方法")
print("意思：向 Claude API 发送请求")
print()
print("代码：response.content")
print("翻译：响应 的 内容")
print("意思：Claude 回复的内容")
print()
print("代码：response.stop_reason")
print("翻译：响应 的 停止原因")
print("意思：Claude 为什么停下来（说完了？要用工具？）")
print()
print("代码：block.type")
print("翻译：内容块 的 类型")
print("意思：这块内容是文字还是工具调用")
print()
print("代码：block.name / block.input / block.id")
print("翻译：工具块 的 名字 / 输入参数 / 编号")
print("意思：要用哪个工具、传什么参数、这次调用的ID")

# === 练习 ===
# 试着创建一个 Product 类，描述你负责的产品
class Product:
    def __init__(self, name, users):
        self.name = name
        self.users = users

    def summary(self):
        return f"产品「{self.name}」，当前用户数 {self.users}"

my_product = Product("在这里写产品名", 10000)
print(f"\n{my_product.summary()}")
