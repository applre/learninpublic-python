# === 第3课：循环 for/while ===
# 让程序学会"重复做事"，不用你一行行写

# 1. for 循环 —— 遍历一个列表
# 列表就是用 [] 括起来的一组数据
fruits = ["苹果", "香蕉", "橘子"]

for fruit in fruits:
    print(f"我喜欢吃{fruit}")

print("---")

# 2. range() —— 生成一串数字
# range(5) 生成 0,1,2,3,4（从0开始，不包含5）
for i in range(5):
    print(f"第{i}次循环")

print("---")

# range 还可以指定起点和步长
# range(起点, 终点, 步长)
for i in range(1, 10, 2):  # 1,3,5,7,9
    print(i, end=" ")  # end=" " 表示不换行，用空格隔开
print()  # 换行

print("---")

# 3. while 循环 —— 条件满足就一直做
# for 是"数着做"，while 是"满足条件就继续做"
count = 0

while count < 3:
    print(f"count = {count}")
    count = count + 1  # 每次 +1，不然会无限循环！

print(f"循环结束，count = {count}")

print("---")

# 4. break —— 提前退出循环
# 找到目标就停下来，不用把剩下的都看完
numbers = [1, 5, 8, 3, 12, 7]

for num in numbers:
    print(f"检查 {num}...")
    if num > 10:
        print(f"找到了大于10的数：{num}！停止搜索")
        break  # 立刻跳出循环

print("---")

# 5. continue —— 跳过这一次，继续下一次
for i in range(1, 6):
    if i == 3:
        print(f"跳过 {i}")
        continue  # 跳过下面的 print，直接进入下一次循环
    print(f"处理 {i}")

print("---")

# 6. 实战：累加求和
# 计算 1+2+3+...+100
total = 0
for i in range(1, 101):  # 1到100
    total = total + i

print(f"1+2+3+...+100 = {total}")

# 7. 实战：九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):  # 循环里套循环（嵌套）
        print(f"{j}×{i}={i*j}", end="\t")  # \t 是制表符，对齐用
    print()  # 每行结束换行

# === 练习 ===
# 用 for 循环打印你最喜欢的5部电影/动漫/游戏
my_favorites = ["在这里写第1个", "第2个", "第3个", "第4个", "第5个"]

print("\n我的最爱TOP5：")
for i, item in enumerate(my_favorites, 1):  # enumerate 同时拿到序号和内容
    print(f"  第{i}名：{item}")
