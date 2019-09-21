#_*_coding=utf-8_*_

from sys import exit


def pass2():
    print "it's buiding..."
    exit(0)
	
def room4():
    print "You are in a bright room."
    print "Here are three fire_birds and the key behind."
    print "The next door was closed."
    
    while True:
        next = raw_input("> ")
    
        if next == "give bugs":
            print "Good job!You are taked the key, move on, Man!"
            next = raw_input("> ")
            
            if next == "open door":
                print "Allright, you are a great Man,欢迎来到代码城。"
                pass2()
            else:
                re_do()
                
        else:
            re_do()
        
        
def road2():
    print "Here are two door to you left and ahead, which one do you choice?"
    
    while True:
        next = raw_input("> ")
    
        if next == "left":
            room4()
        elif next == "ahead":
            dead("You are pierced by arrows!")
        else:
            re_do()


def room3():
    print "There is a bear and some bugs with a key for next door that in the back of bear."
    print "And have a door to you right."
    print "What are you do?"
    
    while True:
        next = raw_input("> ")
        
        if next == "taunt bear":
            print "Good,job! Now the key and bugs you can take."
            
            next = raw_input("> ")
            
            if next == "open door":
                print "The door are openning..."
                road2()
            else:
                re_do()
        
        elif next == "right door":
            gold_room()
        else:
            re_do()
            
def gold_room():
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!\n"
        room3()
    else:
        dead("You greedy bastard!")


def room2():
    print "Here you see the great Six eye o and have a key is behind it."
    print "Do you flee for your life or eat your head?"   
    
    while True:  
        next = raw_input("> ")
     
        if next == "sworded it":
            print "Good job,Man!","Now the key is belongs you."
            print "Now, where are you go? There are nothing."
            
            next = raw_input("> ")
            
            if next == "back":
                road1(True)
            else:
                re_do()
              
        elif next == "flee" or next == "head":
            dead("You were torn to pieces by the Six eye o,")
        else:
            re_do()

def road1(TorF):
    print "You are in a dark road."
    print "There is a door to your right or ahead."
    print "which one do you go?"
    get_key = TorF
    
    while True:
        next = raw_input("> ")
        
        if next == "ahead":
            room2()
            get_key = True
            #print get_key
        elif next == "right" and get_key:
            print "You opened the door with a key, Good job!"
            room3()
        elif next == "right":
            print "You without key of the door."
        else:
            re_do()        

def room1():
    print "You just woke up from a deep dream."
    print "In a dark, a fierce dog guarded the door."
    print "You have a sword and a beef,how do you do?"
    print "kill the dog or give beef to dog?"
    
    while True:
        next = raw_input("> ")
        
        if next == "give beef":
            print "The dog follow you, Good job."
            next = raw_input("> ")
            
            if next == "open door":
                road1(False)
            else:
                re_do()
        
        elif next == "kill":
            print "the door is open."
            print "You've been bitten by the dog."
            
            next =raw_input("> ")
            if next == 1 or True:
                road1(False)
            else:
                dead("致命错误！")
                
        else:
            re_do()
              
def re_do():
    print "Please enter the correct command!"

def dead(why):
    print why, "Good job!"
    exit(0)



print "少年自深梦中苏醒，魔剑持腰，开始踏上缤纷世界。"
next = raw_input("按enter开始游戏......")

if next == "":
    room1()
else:
    exit(0)    

    
