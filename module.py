'''
import math

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))

from math import sqrt
print(sqrt(49))
'''

import random
import string
random_letter = random.choice(string.ascii_letters)
print(random_letter)
print(random.randint(1,50))
small_letter=random.choice(string.ascii_lowercase)
print(small_letter)

capital_letter=random.choice(string.ascii_uppercase)
print(capital_letter)

numbers=[2,3,5,6]
print(random.choice(numbers))

print(random.sample(numbers,k=2))

#try out secret module
'''
import datetime
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(1))
#tryout random date betwwn
from datetime import datetime
now=datetime.now()
curenttime=now.time()
print(curenttime)'''
'''
import sys
print(sys.platform)
print(sys.version)

import os
print(os.getcwd())
print(os.listdir())
import datetime as dt
print(dt.datetime.now())'''


'''
import requests
url=requests.get('https://jsonplaceholder.typicode.com/users/1')
print(url.json())'''
