#coding=utf-8
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count  
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#下面都调用上面定义的函数（cheese_and_crackers） 
#将（）里的参数代入定义的函数中，每次都运行一遍函数中的内容
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 +6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
-----------------------------------------------------------------------
-----------------------------------------------------------------------
通过这个练习，可以看到赋予了函数 cheese_and_crackers 很多参数，如何在函数里
把他们打印出来。
    1.在函数里可以用变量名 % (cheese_count, boxes_of_crackers)
    2.可以在函数里运算--->>>(10+20, 5+6)
    3.可以将变量和运算结合起来--->>>(amount_of_cheese + 100)
    
