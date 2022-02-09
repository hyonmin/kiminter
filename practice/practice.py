from math import *
print(floor(3.4134))

from random import *
print(random())
print(random()*10)
print(int(random()*10))
print(int(random()*10) + 1)


print(int(random()*45)+1)

print(randrange(1, 46))

print(randint(1,45))

'''
Q1) you have made a group for a study. you should make 4 meetings, 3 times for online, 1 time for offline.
Make a code to make a decision what date you gonna do a offline meeting.

condition 1: choose a date randomly
condition 2: It is different how many days each month has. Just let the days 28.
condition 3: from first day to third day for each month, you should prepare the meetings. So you should make the code not to choose
them.
'''

from random import *

x = randint(4,28)
print('The meeting is on the ' + str(x) + ' of every month.')


sentence = 'I am a boy'
print(sentence)
sentence2 = 'Python is easy'
print(sentence2)
sentence3 = '''
I am a boy and,
Python is easy
'''
print(sentence3)


python = 'python is amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'Java'))

index = python.index('n')
print(index)
index = python.index('n', index + 1)
print(index)

print(python.find('Java'))


# print(python.index('Java') will make an error.
print(python.count('n'))


print("I am %d." %20) # only integer
print('I like %s.' %"an apple") # only string
print('Apple begin with %c' % "A") # only one character allowed
 
# %s covers all things
print("I am %s." %20)
print("I like %s and %s colors." % ("red", "blue"))

# {} covers all things
print("I love {} and {} colors." .format('blue', 'red'))
print("I like {0} and {1} colors." .format('blue', 'red'))
print("I like {1} and {0} colors." .format('blue', 'red'))

print('I am {age} and I like {color}.' .format(age = 20, color='red'))

# ver3.6~
age = 20
color = 'red'
print(f'I am {age} and I like {color}')


# \r move the cursor to the first place and then change the write mode into insert.
print("red apple\rPine")
# \b backspace
# \t tap key


'''
Q2) make a code to create passwords for each site.
ex) http://www.naver.com
condition 1: subtract 'http://www.' -> naver.com
condition 2: subtract all letters after the dot and the dot it self. -> naver
condition 3: the first three letters + the number of the letters + the number of letter 'e' + '!'
-> the password will be "nav51!"
'''

site = 'http://www.nate.com'
find1 = site.find('.')
find2 = site.find('.', find1 + 1)
pass1 = site[find1 + 1 : find2]
print(pass1[:3] + str(len(pass1)) + str(pass1.count('e' )) + '!')


def characterFinder(c):
    n = site.count(c)
    res = []
    index = -1
    for i in range(n):
	    index = site.index(c, index + 1)
	    res.append(index)

    print(res)
    
    
print(site.find("."))
