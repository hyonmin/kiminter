'''
Q5) Let you a taxi driver using COCOA matching service.
There are matching chances to have 50 people.
Make a code to choose proper passengers under the conditions below.

condition 1: the time required for each passenger would be 5~50 minutes randomly.
condition 2: you can have passengers of the time required 5~15 minutes only.

ex)
[o] 1st passenger (the time required: 15 mins)
[ ] 2nd passenger (the time required: 50 mins)
[o] 3rd passenger (the time required: 5 mins)
...
[ ] 50th passsenger (the time required: 16 mins)

The amount of passengers: 2 people
'''

psg_avl=0	

from random import *

for i in range(1,51):
	mins = randint(5,50)
	if mins >= 5 and mins <=15:
		ox = 'o'
		psg_avl += 1
	else:
		ox = ' '
	print('[{0}] passenger No. {1} (the time required: {2} mins)' .format(ox, i, mins))
	i += 1

print("The amount of passengers: %s people" % psg_avl)
