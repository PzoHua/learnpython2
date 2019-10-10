import room4

def road():
    print "Here are two door to you left and ahead, which one do you choice?"
    
    while True:
    
        next = raw_input("> ")
        if next == "left":
            room4.room()
        elif next == "ahead":
            dead("You are pierced by arrows!")
        else:
            re_do()
def re_do():
    print "Please enter the correct command!"
