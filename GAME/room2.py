import road1
def room():
    print "Here you see the great Six eye o and have a key is behind it."
    print "Do you flee for your life or eat your head?"   
    
    while True:  
    
        next = raw_input("> ")
        if next == "kill it":
            print "Good job,Man!","Now the key is belongs you."
            print "Now, where are you go? There are nothing."
            
            next = raw_input("> ")
            
            if next == "back":
                ro = road1.need_key()
                ro.road(True)
                
            else:
                re_do()
              
        elif next == "flee" or next == "head":
            dead("You were torn to pieces by the Six eye o,")
        else:
            re_do()

def re_do():
    print "Please enter the correct command!"
    
def dead(why):
    print why, "Good job!"
    exit(0)
