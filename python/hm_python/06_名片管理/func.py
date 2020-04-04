#!/usr/bin/env python
# coding=utf-8

cards = []

def display_menu():
    """1.显示菜单""" 
    print("*" * 50)
    print("欢迎使用名片系统v1.0")
    print("\n1.增加名片")
    print("2.查看所有名片")
    print("3.搜索名片\n")
    print("0.退出系统")
    print("*" * 50)


def add_card():
    """2.增加名片"""
    name = str(input(">>>请输入名字："))
    phone = int(input(">>>请输入电话："))
    qq_num = int(input(">>>请输入QQ："))
    mail = str(input(">>>请输入邮箱："))
    card = {"name":name,
            "phone":phone,
            "qq_num":qq_num,
            "mail":mail}
    cards.append(card)


def display_cards():
    """3.显示所有名片""" 
    if len(cards) == 0:
        print("没有名片记录，请新增名片")
        return
    print("-" * 50)
    print("名字\t\t电话\t\tQQ\t\t邮箱")
    print("=" * 50)
    for card in cards:
        print("%s\t\t%d\t\t%d\t\t%s" % (card["name"], card["phone"], card["qq_num"], card["mail"]) )
    print("-" * 50)


def searce_card(name):
    """4.搜索名片"""
    for card in cards:
        if card['name'] == name:
            print("名字\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%d\t\t%d\t\t%s" % (card["name"], card["phone"], card["qq_num"], card["mail"]) )
            print("=" * 50)
            break
    else:
        print("未查询到%s" % name)
        return

    action = input(">>>请输入操作功能(1--修改 2--删除 0--返回)：")
    print("您选择的功能是 %s" % action)
    
    if action == "0":
        return

    elif action == "1":
        card['name'] = input_card_info(card['name'], ">>>请输入名字：")
        card['phone'] = int(input_card_info(card['phone'], ">>>请输入电话："))
        card['qq_num'] = int(input_card_info(card['qq_num'], ">>>请输入QQ："))
        card['mail'] = input_card_info(card['mail'], ">>>请输入邮箱：")
        print("修改名片成功！")

    elif action == "2":
        cards.remove(card)
        print("删除名片成功！")

    else:
        print("输入错误，请重新输入")


def input_card_info(dict_value, tip_message):
    result_str= input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value

