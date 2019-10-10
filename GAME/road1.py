import room2, room3

class need_key():

    def road(self, key):
        print "You are in a dark road."
        print "There is a door to your right or ahead."
        print "which one do you go?"
        get_key = key
        
        while True:

            next = raw_input("> ")
            if next == "ahead":
                room = room2.room()
                get_key = True
                #print get_key
            elif next == "right" and get_key:
                print "You opened the door with a key, Good job!"
                room = room3.room()
            elif next == "right":
                print "You without key of the door."
            else:
                re_do()

def re_do():
    print "Please enter the correct command!"

