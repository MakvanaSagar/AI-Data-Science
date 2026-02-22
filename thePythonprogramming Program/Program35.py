
#=======================================================OOP CONSEPT IN PTHON===================================================



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[1: Class and Object]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
class myClass: 				#create a class
	Player_name = ""	
	Jursy_no = 0			#this value access using object

myObj1 = myClass()			#create a object
myObj1.Player_name = "Rohit sharma"
myObj1.Jursy_no = 45

myObj2 = myClass()			#create a object
myObj2.Player_name = "Virat kohli"
myObj2.Jursy_no = 18

myObj3 = myClass()			#create a object
myObj3.Player_name = "MS Dhoni"
myObj3.Jursy_no = 7

print(f"Player_name = {myObj1.Player_name} and Jursy_no = {myObj1.Jursy_no}")
print(f"Player_name = {myObj2.Player_name}  and Jursy_no = {myObj2.Jursy_no}")
print(f"Player_name = {myObj3.Player_name}     and Jursy_no = {myObj3.Jursy_no}")
'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[2: Inheritance]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''
############ Example:1

class Parent:
	
	def myFun(self):
		x = 0
		y = 0
		

class Child(Parent):
	
	def myFunn(self):
		z = 0

f1 = Child()
f2 = Child()
f3 = Child()

f1.Child = 7328
f2.Child = 36283

print(f"Number + Numbers = {f1.Child + f2.Child}")



############ Example:2

class Fruits:
	def apple(self):
		print("Hey, guy i am a Apple!")
	def banana(self):
		print("Hey, guy i am a Banana!")

class Vegitables(Fruits):
	def tomato(self):
		print("Hello, everybady my color is Red and I am Tomato!")

myObj = Vegitables()

myObj.apple()
myObj.banana()
myObj.tomato()
'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[3: Polymorphism]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Polygon:
    
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
   
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    
    def render(self):
        print("Rendering Circle...")
    

s1 = Square()
s1.render()


c1 = Circle()
c1.render()
