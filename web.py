__author__ = 'apple'

# This file editor by PyCharm

import sys
import requests
import httplib
import webbrowser
import sqlite3


# name = raw_input("What is your name? ")
# print(name)

edward = ['Edward Gumby',42]
john = ['John smith',50]
database = [edward,john]
print(database)

greeting = 'Hello'
print(greeting[-3])

numbers = [1,2,3,4,5,6,7,8,9,10]
print('[3] is', numbers[3])
print('[6] is', numbers[6])
print('To last', numbers[3:])
print('From first', numbers[:3])

# set step length
print(numbers[0:10:2])
print(numbers[::3])

# webbrowser.open('http://www.python.org')