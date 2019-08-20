# raw_input("what your questions?")
age = raw_input("How old are you?\t\b")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

print "So, you are %r old, %r tall and %r heavy." % (
   age, height, weight)



--------------------------------------------------------------------------------------------------------
#raw_input()中()的作用
print "How old are you?",
age = raw_input()
等价于：
age = raw_input("How old are you?")
