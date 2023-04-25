# 编辑者：小手哈哈哈
# 开发时间：2023/1/4 23:07

# print函数使用

# print(520)
# print("helloworld")
# print('helloworld')  # 单双引号都可以
# print(5+6)

# # """三个引号代表多行注释


# # 查看数据变量类型

# print(type("小手哈哈哈"))
# print(type(6.66))
# print(type(1))

# # 数据类型转换

# num_str = str(11)
# print(type(num_str), num_str)

# num = int("11")
# print(type(num), num)

# num = float("11")
# print(type(num), num)


# # 字符串拼接
# num = 33

# print("我的年龄是%s岁" % num)
# print(f"我的年龄是{num}岁")


# 数据输入input,默认输入的都是字符串
# name = input()
# print("name:%s" % name)
# user_name = input("请输入用户名：")
# number = input("请输入账号：")
# print(f"你好{user_name}, 您是尊贵的{number}用户，欢迎光临")


# for循环
name = "fjkfaaafjkdjfkaaafka"
count = 0
for x in name:
    if(x == "a"):
        count += 1
print(f"a的个数有{count}个")
