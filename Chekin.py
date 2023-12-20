'''import Module1
print(Module1.mult(9,9))
print(Module1.sum(100,100))

# using alias name
import Module1 as m
print(m.sum(90,9))
print(m.mult(100,90))'''


# using from
'''from Module1 import sum
print(sum(100,20))

from Module1 import *
print(sum(10,20))
print(mult(10,10))'''

# ceil float ko change kr k aage bali value m pahucha deta h
'''import math
x = 11.2
print(math.ceil(x))'''

# Fabs  //negative value nhi deta
'''import math
x = -10
print(math.fabs(x))'''

# factorial
'''import math
print(math.factorial(10))
y = 100.5 # peeche ki value date h
print(math.floor(y))
z = [1,2,3,4,5] # list k elements ka sum deta h float m
print(math.fsum(z))
s = 81  ## konsi value ks sq root 81 h
print(math.sqrt(s))'''

#random module
# random.randit()
import random
x = print(random.randint(2,8)) # random number genrate krta h
x = print(random.randint(1,100))

# randrange
'''n1 = random.randrange(2,4)
print(n1)
# choice
l= ["ram","shyam","shivam"]
lc = random.choice(l)
print(lc)'''

#suffle  list k ele koi se bhi num p aa skta h
l = [1,2,3,4,4]
random.shuffle(l)
print(l)

# uniform  float value dega
u = random.uniform(3,9)
print(u)





