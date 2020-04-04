has_ticket = True
knife_length = 18

if has_ticket:
    print("车票检查通过，准备安检")
    if knife_length < 20:
        print("请进站")
    else:
        print("拿长刀，请滚出去")
else:
    print("没票，滚蛋")
