from sys import exit
import room3

def gold():
    print "This room is full of gold.  How much do you take?"
    list = []
    for i in range(0,100,10):
        list.append(i)
    print list
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!\n"
        room3.room()
    else:
        dead("You greedy bastard!")

def dead(why):
    print why, "Good job!"
    exit(0)
