
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for_loop goes through a list 
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range funtion to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
    
# now we can print them out too
for i in elements:
    print "Element was: %d" % i

-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
range用法：
Python range() 函数可创建一个整数列表，一般用在 for 循环中。

函数语法
range(start, stop[, step])

参数说明：
    start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
    stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
    step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
    
注意：如果要倒数，如列表：[10，8，6，4，2]  则是 range(10, 0, -2)；没有0，每次递减2。
    
来源：https://www.runoob.com/python/python-func-range.html


















