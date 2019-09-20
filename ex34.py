
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']


print """
animals = %s
The animal at 1: %s
The 3rd animal:  %s
The 1st animal:  %s
The animal at 3: %s
The 5th animal:  %s
The animal at 2: %s
The 6th animal:  %s
The animal at 4: %s
"""  % (animals, animals[1], animals[2], animals[0], 
animals[3], animals[4], animals[2], animals[5], animals[4])

------------------------------------------------------------------------------
------------------------------------------------------------------------------
练习访问列表中的元素：
该列表animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']共有六个元素
注意：抓取第一个元素是animals[0], 而不是animals[1]

animals[0]-->>对应元素'bear'        --->>第一个元素
animals[1]-->>对应元素'python'      --->>第二个元素
animals[2]-->>对应元素'peacock'     --->>第三个元素
animals[3]-->>对应元素'kangaroo'    --->>第四个元素
animals[4]-->>对应元素'whale'       --->>第五个元素
animals[5]-->>对应元素'platypus'    --->>第六个元素
来源：《笨办法学Python》（习题34）
