#_*_coding=utf-8_*_

# 系统模组今古印
from sys import exit

# 贪狼尸首黄金屋
def gold_room():
    print "This room is full of gold.  How much do you take?"
	
    next = raw_input("> ")
    if "0" in next or "1" in next:
	    how_much = int(next)
    else:
	    dead("Man, learn to type a number.")
		
    if how_much < 50:
	    print "Nice, you're not greedy, you win!"
	    exit(0)
    else:
	    dead("You greedy bastard!")

# 蜂蜜熊吼葬熊房 弄熊得进黄金屋
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
	
    while True:
	    next = raw_input("> ")
		
	    if next == "take honey":
		    dead("The bear looks at you then slaps your face off.")
	    elif next == "taunt bear" and not bear_moved:
		    print "The bear has moved from the door. You can go through it now."
		    bear_moved = True
	    elif next == "open door" and bear_moved:
		    gold_room()
	    else:
		    print "I got no idea what that means."

# 克鲁门开生死劫 首悬半空足前倾
def cthulhu_room():
    print "Here you see  the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
	
    next = raw_input("> ")
	
    if "flee" in next:
	    start()
    elif "head" in next:
	    dead("Well that was tasty!")
    else:
	    cthulhu_room()
		
# 生机掩鬼魂魄现
def dead(why):
    print why, "Good job!"
    exit(0)

# 暗门左右游戏开
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
	
    next = raw_input("> ")
	
    if next == "left":
	    bear_room()
    elif next == "right":
	    cthulhu_room()
    else:
	    dead("You stumble around the room until you starve.")
		
start()

-------------------------------------------------------------------
-------------------------------------------------------------------
这是一个小游戏程序：
1.运行该程序开始进入start()函数，提示用户进左门还是右门（要求输入right或left），然后通过if语句判断哪个为真（跟用户输入得字符串比较）；
   1.1.如果是left则进入bear_room()函数中，要移动熊才能打开熊后面得门，且熊有一罐蜂蜜；输入take honey 则结束游戏；输入taunt bear则进入黄金
   屋（gold_room),其他输入则提示用户无法理解该含义；
   1.2.如果是right则进入cthulhu_room()（邪神门），此时有两个选择flee或head，flee回到stare()函数，head则结束游戏；
2.如果进了left门，且成功移动了熊（即输入了taunt bear），再次输入open door进入黄金屋（gold_room),问你要拿走多少黄金，输入1 or 0则获胜。














