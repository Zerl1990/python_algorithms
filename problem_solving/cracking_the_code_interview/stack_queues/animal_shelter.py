# Animal Shelter: An animal shelter, which holds only dogs and cats, operates
# on a strictly first in, first out basis.
# People must adopt either the oldest based on arrival date of all
# animals at the shelter, or the can select whether they would prefer a dog or cat
# (and will receive the oldest animal of that type). They cannot select which
# specific animal they would like. Create the data structure
# to maintain this system and impelment operations such as enqueue, dequeue_any
# dequeue_dog and dequeue_cat.
import os
import sys

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class AnimalShelter(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, animal):
        if not self.head:
            self.head = Node(animal)
            self.tail = self.head
        else:
            self.tail.next = Node(animal)
            self.tail = self.tail.next

    def dequeue_any(self):
        animal = self.head
        self.head = self.head.next
        animal.next = None
        return animal.value
        

    def dequeue_dog(self):
        return self.__dequeue_animal('DOG')

    def dequeue_cat(self):
        return self.__dequeue_animal('CAT')

    def __dequeue_animal(self, animal_type):
        it = self.head

        # Simple case, just dequeue
        if it.value == animal_type:
            return self.dequeue_any()

        # Search animal
        while it.next and it.next.value != animal_type:
            it = it.next

        if not it.next:
            return None
        else:
            animal = it.next.value
            #Remove that animal
            to_remove = it.next
            it.next = to_remove.next
            to_remove.next = None
            return animal

    def empty(self):
        return self.head == None


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('CAT')
    shelter.enqueue('DOG')
    shelter.enqueue('CAT')
    shelter.enqueue('CAT')
    shelter.enqueue('CAT')
    shelter.enqueue('CAT')
    shelter.enqueue('DOG')
    print shelter.dequeue_dog()
    print shelter.dequeue_dog()
    print shelter.dequeue_dog()
    
    
