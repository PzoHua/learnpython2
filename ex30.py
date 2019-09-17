# if--elif--else

people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."   #line1
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
   
if buses > cars:
    print "That's too many buses."
elif buses < cars:                      
    print "Maybe we could take the buses."   #line2
else:
    print "We still can't decide."
	
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."       #line3

---------------------------------------------------------
运行结果：
PS C:\work> python ex30.py
We should take the cars.
Maybe we could take the buses.
Alright, let's just take the buses.
PS C:\work>
---------------------------------------------------------
如果多个elif区块都是True时Py't'hon会如何处理？
---->>>Python只会运行它碰到的是True的第一区块，所以只有第一个True的区块会被运行。
