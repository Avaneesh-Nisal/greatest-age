# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:14:32 2020

@author: amolb
"""


user1 = input('What is age of the first user:  ')
user2 = input('What is age of the second user: ')
user3 = input('What is age of the third user:  ')

if user1 > user2 and user1 > user3:
    print('User 1 has smallest age')
elif user2 > user1 and user2 > user3:
    print('User 2 has smallest age')
elif user3 > user1 and user3 > user2:
    print('User 3 has smallest age')
else:
    print('Ages are equal')