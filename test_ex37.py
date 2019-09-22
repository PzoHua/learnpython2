var = 1

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
        
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
    
while var == 1 :
    num1 = raw_input("Enter num1: ")
    num2 = raw_input("Enter num2: ")
    if is_number(num1) and is_number(num2):
        sum = int(num1)+int(num2)
        print "output sum:%s+%s=%s\n" % (num1, num2, sum)
    else:
        print "Please enter number."
        continue
print "Good bye"

------------------------------------
测试while循环，is（对象判断），同时也是个简单的加法计数器。
