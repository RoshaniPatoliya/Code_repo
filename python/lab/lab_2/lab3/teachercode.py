"""class Circle():
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * Circle.pi
    def setRadius(self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
c = Circle()
c.setRadius(2)
print('Radius is: ', c.getRadius())
print('Area is: ',c.area())
class Animal():
    def __init__(self):
        print("Animal created")
    def __whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating..nom nom..")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def whoAmI(self):
        print("Dog")
    def bark(self):
        print("Woof woof!")    
d = Dog()
d.whoAmI()
d.eat()
d.bark()
class Book():
    def __init__(self,title,author,pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title:%s, author:%s, pages:%s" %(self.title, self.author, self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book is destroyed")
book = Book("Python", "John Andersson", 180)
#print(book)
del book
"""
#try and except
#try:
#Operations here...
#except: 
#if there is an exception then execute this block...
#except: 
#else:
try:
    f = open('testfile', 'r')
    f.write('Test write this...')
except:
    print("Error.. Could not read file..")
finally:
    print('Always execute finnaly code blocks')
    f.close()