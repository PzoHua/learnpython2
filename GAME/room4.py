#_*_coding=utf-8_*_
import pass2

def room():
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
                pass2.pass_2()
            else:
                re_do()
                
        else:
            re_do()
                    
def re_do():
    print "Please enter the correct command!"
