import os
import sys

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age



luis = Student('luis', 27)
lulu = Student('lulu', 18)
queue = []
queue.append(luis)
queue.append(lulu)
my_dict = {}
my_dict['luis'] = luis
my_dict['lulu'] = lulu

my_dict['luis'].age = 40

print queue[0].age
print luis.age
