#_*_coding=utf-8_*_
# 布尔表达式练习

True and True                                                            #True
False and True                                                           #False
1 == 1 and 2 == 1                                                        #False
"test" == "test"                                                         #True
1 == 1 or 2 != 1                                                         #True
True and 1 == 1                                                          #True
False and 0 != 0                                                         #False
True or 1 == 1                                                           #True
"test" == "testing"                                                      #False
"test" == 1                                                              #False
"testing" != "test"                                                      #True
"test" == 1                                                              #False
not (True and False)                                                     #True
not (1 == 1 and 0 != 1)                                                  #False        
not (10 == 1 or 1000 == 1000)                                            #False
not (1 != 10 or 3 == 4)                                                  #False
not ("testing" == "testing" and "Zed" == "Cool Guy")                     #True
1 == 1 and not ("testing" ==1 or 1==0)                                   #Ture
"chunky" == "bacon" and not (3 == 4 or 3 == 3)                           #False
3 == 3 and  not ("testing" == "testing" or "Python" == "Fun")            #False



--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
PS C:\work> python
Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> False and True
False
>>> 1 == 1 and 2 == 1
False
>>> "test" == "test"
True
>>> 1 == 1 or 2 != 1
True
>>> True and 1 == 1
True
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> "test" == "testing"
False
>>> "test" == 1
False
>>> "testing" != "test"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1 == 1 and 0 != 1)
False
>>> not (10 == 1 or 1000 == 1000)
False
>>> not (1 != 10 or 3 == 4)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and not ("testing" ==1 or 1==0)
True
>>> "chunky" == "bacon" and not (3 == 4 or 3 == 3)
False
>>> 3 == 3 and  not ("testing" == "testing" or "Python" == "Fun")
False
>>> ^Z

PS C:\work>
