
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

