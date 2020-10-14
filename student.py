data=[
    {
        'name':'Susan',
        'age':13
    }
]

#输入名字的优化 （不输入和输入空格的去除）
def input_name():
    while True:
        name = input("请输入名字：").strip() #strip()是去除头尾的空格
        if name: # 如果有输入名字，就返回名字
            return name
        else:
            continue
# 选择性别
def
