class Animal:
    def __init__(self,name):
        self.name = name
    def walk(self):
        print('{} is walking'.format(self.name))
class Dog(Animal):
    def bark(self):
        print('woof')

if __name__ == "__main__":
  a = Animal('giraffe')               # We do not pass any argument to the __init__ method
  a.walk()   
  b = Dog(a)         # We only pass a single argument
  b.bark()