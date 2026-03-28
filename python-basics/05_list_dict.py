# === 第5课：列表和字典 ===
# 列表 = 有序的一组数据（用 []）
# 字典 = 一组"键值对"（用 {}）

# ============ 第一部分：列表 list ============

# 1. 创建列表
fruits = ["苹果", "香蕉", "橘子"]
numbers = [1, 2, 3, 4, 5]
mixed = ["小白", 25, True, 3.14]  # 可以混着放

print(fruits)
print(f"列表里有 {len(fruits)} 个元素")  # len() 获取长度

print("---")

# 2. 取值 —— 用下标（从0开始！）
print(f"第1个水果：{fruits[0]}")  # 0 = 第一个
print(f"第2个水果：{fruits[1]}")  # 1 = 第二个
print(f"最后一个：{fruits[-1]}")  # -1 = 倒数第一个

print("---")

# 3. 修改、添加、删除
fruits[0] = "草莓"        # 修改第1个
print(f"修改后：{fruits}")

fruits.append("西瓜")     # 末尾添加
print(f"添加后：{fruits}")

fruits.remove("香蕉")     # 删除指定元素
print(f"删除后：{fruits}")

print("---")

# 4. 遍历列表（第3课学的 for 循环）
for fruit in fruits:
    print(f"  我有：{fruit}")

print("---")

# ============ 第二部分：字典 dict ============

# 5. 创建字典 —— "键: 值" 的组合
# 就像一本通讯录：名字 → 电话号码
person = {
    "name": "小白",
    "age": 25,
    "job": "产品经理",
    "hobby": "coding",
}
print(person)

print("---")

# 6. 取值 —— 用"键"来取
print(f"名字：{person['name']}")
print(f"职业：{person['job']}")

print("---")

# 7. 修改、添加、删除
person["age"] = 26             # 修改
person["city"] = "北京"         # 添加新的键值对
del person["hobby"]            # 删除
print(f"更新后：{person}")

print("---")

# 8. 遍历字典
for key, value in person.items():
    print(f"  {key} → {value}")

print("---")

# ============ 第三部分：组合使用 ============

# 9. 列表里套字典 —— 最常见的数据结构！
team = [
    {"name": "小白", "role": "产品经理"},
    {"name": "小李", "role": "设计师"},
    {"name": "小张", "role": "工程师"},
]

for member in team:
    print(f"  {member['name']} - {member['role']}")

print("---")

# 10. 回看 agent_loop —— 现在你能看懂更多了！
#
# messages 就是一个"列表里套字典"：
messages = [
    {"role": "user", "content": "北京天气怎么样？"},
    {"role": "assistant", "content": "我来帮你查一下"},
]

# messages.append(...) 就是往列表末尾加一条新消息：
messages.append({"role": "user", "content": "谢谢"})

print("messages 对话记录：")
for msg in messages:
    role = "你" if msg["role"] == "user" else "AI"
    print(f"  {role}：{msg['content']}")

print("---")

# 11. 字典取值的另一种写法
tool_result = {
    "type": "tool_result",
    "tool_use_id": "abc123",
    "content": "北京 32°C 晴",
}
print(f"类型：{tool_result['type']}")
print(f"内容：{tool_result['content']}")

# === 练习 ===
# 创建你自己的"个人资料卡"
my_profile = {
    "name": "在这里写你的名字",
    "job": "在这里写你的职业",
    "skills": ["技能1", "技能2", "技能3"],  # 列表也能当值！
}

print(f"\n个人资料：")
print(f"  姓名：{my_profile['name']}")
print(f"  职业：{my_profile['job']}")
print(f"  技能：{'、'.join(my_profile['skills'])}")  # join 把列表连成字符串
