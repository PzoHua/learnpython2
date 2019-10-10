import road2, gold_room

def room():
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
                road2.road()
            else:
                re_do()
        
        elif next == "right":
            gold_room.gold()
        else:
            re_do()
            
def re_do():
    print "Please enter the correct command!"
