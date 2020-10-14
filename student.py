#学生信息
data=[
    {
        "name":"Tommy",
        "age":18,
        "sex":"男"
    },
    {
        "name": "Susan",
        "age": 14,
        "sex": "女"
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


def beauty_output(data):
    for index,student in enumerate(data):
        print(f'序号:{index}',end='\t')
        print(f'姓名:{student["name"]}',end='\t')
        print(f'年龄:{student["age"]}',end='\t')
        print(f'性别:{student["sex"]}')


#1.显示所有学生信息
def selectAll():
    beauty_output(data)

#2.新建学生信息
def addStudent():
    name = input("请输入新增学生的姓名：")
    age = input("请输入新增学生的年龄：")
    sex = input("请输入新增学生的性别：")
    data.append({'name':name,'age':age,'sex':sex})

#3.查询学生信息
def searchStudent():
    name = input("请输入您要查询的学生姓名:")
    for student in data:
        if student['name']==name:
            print(student)
            return
    else:
        print("查无此人")

# 4.修改学生信息
def updateStudent():
    name = input("请输入您要修改的学生姓名:")
    for student in data:
        if student['name'] == name:
            student['name'] = input("请输入您要修改的名字：")
            student['age'] = input("请输入您要修改的年龄：")
            student['sex'] = input("请输入您要修改的性别：")
            return
    else:
        print("查无此人")


# 5.删除学生信息
def deleteStudent():
    name = input("请输入您要删除的学生姓名：")
    for student in data:
        if student['name'] == name:
            data.remove(student)
            return
    else:
         print("查无此人")




while True:
    print("""
    ***************学生垃圾管理系统***************
    1.显示所有学生信息
    2.新建学生信息
    3.查询学生信息
    4.修改学生信息
    5.删除学生信息
    0.退出系统
    ********************************************** 
    """)
    op = input("请输入数字操作")
    if op=='1':
        selectAll()
    elif op=='2':
        addStudent()
    elif op == '3':
        searchStudent()
    elif op == '4':
        updateStudent()
    elif op == '5':
        deleteStudent()
    elif op == '0':
        print("退出系统")
        break
