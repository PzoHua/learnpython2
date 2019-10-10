#_*_coding=utf-8_*_
import road1
from sys import exit

class dog_room():

    def beef(self):
        list_print = [ "You just woke up from a deep dream.",
         "In a dark, a fierce dog guarded the door.",
         "You have a sword and a beef,how do you do?",
         "kill the dog or give beef to dog?"]
         
        for i in list_print:
            print i
        
        while True:
        
            next = raw_input("> ")
            if next == "give beef":
                print "The dog follow you, Good job."
                next = raw_input("> ")
                
                if next == "open door":
                    ro = road1.need_key()
                    ro.road()
                else:
                    re_do()
            
            elif next == "kill":
                print "the door is open."
                print "You've been bitten by the dog."
                
                next = raw_input("> ")
                if next == 1 or True:
                    ro = road1.need_key()
                    ro.road(False)
                else:
                    dead("致命错误！")
                    
            else:
                re_do()

def re_do():
    print "Please enter the correct command!"
    
def dead(why):
    print why, "Good job!"
    exit(0)
