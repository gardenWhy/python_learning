#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
1、可以支持以下搜索语法
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT" //dept：部门
find * from staff_table were enroll_data like "2013" //enroll_data：入职日期

2、可以创建新的员工信息,以Phone做唯一键（即不允许表里有手机号重复的情况）,staff_id需要自增
add staff Alex Li,25,134435344,IT,2015-10-29

3、可以删除指定的员工信息，输入id直接删除
del staff 3

4、可以修改员工信息，
UPDATE staff_table SET dept="Market" WHERE dept="IT" //把所有dept为IT的记录的信息改为Market

'''


def init_file():
    with open('员工信息表.txt', 'r+', encoding='utf-8') as staff_infofile:
        data_staff = {}
        staff_list = ['id', 'name', 'age', 'phone', 'depart', 'enrolled_date']
        for i in staff_list:
            data_staff[i] = []
        for line in staff_infofile:
            staff_id, staff_name, staff_age, staff_phone, staff_depart, staff_date = line.split(',')
            data_staff['id'].append(staff_id)
            data_staff['name'].append(staff_name)
            data_staff['age'].append(staff_age)
            data_staff['phone'].append(staff_phone)
            data_staff['depart'].append(staff_depart)
            data_staff['enrolled_date'].append(staff_date)
    return data_staff
DATA_STAFF = init_file()
#进行文件读取初始化

def welcome():
    print('''
    欢迎来到员工信息查询系统！
        操作选项：
        1、查询员工信息
        2、新增员工信息
        3、删除员工信息
        4、修改员工信息 
        5、显示现有员工信息   
        ''')


def search():
    print('''   
      -------------------欢迎进入员工信息查询界面-----------------
      ********************************************************
                            命令行示例
      find name,age from staff_table where age > 22
      find * from staff_table where dept = "IT" 
      find * from staff_table were enroll_data like "2013" 
      ********************************************************
      
      ''')
    while True:
        user_input = ("请输入你的查询语句（返回上一层，请输入q）:").split()


def create():
    print('''
    -------------------欢迎进入员工信息创建界面-----------------
    ********************************************************
                          命令行示例
    add staff Alex Li,25,134435344,IT,2015-10-29
    ********************************************************
    请输入你的创建语句（返回上一层，请输入q）
    ''')


def delete():
    print('''
   -------------------欢迎进入员工信息删除界面-----------------
   ********************************************************
                         命令行示例
    del staff 3
   ********************************************************
   请输入你的删除语句（返回上一层，请输入q）
   ''')


def updata():
    print('''
   -------------------欢迎进入员工信息更新界面-----------------
   ********************************************************
                         命令行示例
   UPDATE staff_table SET dept="Market" WHERE dept="IT"
   ********************************************************
   请输入你的更新语句（返回上一层，请输入q）
   ''')


def show():
    pass


def main():
    while True:
        welcome()
        sign = input('请输入要执行的操作选项 >>')
        user_actions = {
            1: search,
            2: create,
            3: delete,
            4: updata,
            5: show,
        }
        if sign.isdigit():
            if sign.isdigit() in user_actions.keys():
                user_action = user_actions[sign.isdigit()]
                user_action()
        else:
            print("输入错误！请重新输入！")


if __name__ == '__main__':
    main()
