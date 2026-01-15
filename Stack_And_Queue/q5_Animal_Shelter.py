# INTERVIEW QUESTION 5: ANIMAL SHELTER

# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
# People must adopt either the "oldest" (based on arrival time) of all the animals at the shelter, 
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. 
# Create the data structures to maintain this system and implement operations such as enqueue, dequeue, dequeueAny, 
# dequeueDog and dequeueCat.


class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []


    def enqueue(self, animal, type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)


    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat
        

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog
        
    
    def dequeueAny(self):
        if len(self.cats) > 0:
            result = self.cats.pop(0)
        else:
            result = self.dogs.pop(0)
        return result
    

customQueue = AnimalShelter()
customQueue.enqueue("Cat1", "Cat")
customQueue.enqueue("Cat2", "Cat")
customQueue.enqueue("Dog1", "Dog")
customQueue.enqueue("Cat3", "Cat")
customQueue.enqueue("Dog2", "Dog")
customQueue.enqueue("Dog3", "Dog")
print(customQueue.dequeueCat())
print(customQueue.dequeueDog())
print(customQueue.dequeueAny())



