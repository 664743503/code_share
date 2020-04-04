#!/usr/bin/python3
# coding=utf-8
from func import *

def main():
    while True:
        display_menu()
        action = input(">>>请输入操作功能：")
        print("您选择的功能是 %s" % action)
    
        if action == "0":
            break

        elif action == "1":
            add_card()
            print("增加名片成功！")
    
        elif action == "2":
            display_cards()
    
        elif action == "3":
            name = str(input(">>>请输入名字："))
            searce_card(name)
        else:
            print("输入错误，请重新输入")
    
    
main()
