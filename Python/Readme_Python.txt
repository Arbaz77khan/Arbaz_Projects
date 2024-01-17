-----------------------------------786---------------------------------------------------

Python version 3.11.5
PIP version 23.2.1

PEP 8 is the style guide for Python code. It provides conventions for writing clean and readable code.

Naming convention for class : CapWords convention, also known as CamelCase. This means that the names of classes should capitalize the first letter of each word, without underscores between words. For example: MyClass

Naming convention for function, variable : lowercase letters with underscores between words. This convention is known as "snake_case." For example: calculate_sum


---***Python is case sensitive****----------------

Extension - .py

Modules : It is a file containing code written by someboby else which can be imported and used in program.

PIP : It is a package manager for python used to install a module.

Example-

				Module : 	import os

				PIP : 		pip install flask
				
Types of module - 

		Build-in module : Pre installed in python (e.g - import os)
		External module : Need to install using pip (e.g - import flask)

REPL : we can also write a code in terminal. simply add initial command "python" and then start executing code. This way is called as REPL i.e read-execute-print-loop. To exit REPL command "exit()".

Comments-

		Single line comment : # (shortcut key = ctrl + /)
		Multiline comment : ''' xyz '''
		In VS code : to comment multiline press ctrl + /

Multi Line Print :
					print('''abc
							xyz''')		

Variable Types :  (variable name cannot start with digit)(variable names are case sensitive)
				a = "Arbaz"
				b = 'Hasmuddin'
				c = '''My 'name' is "khan" '''
				d = 123
				e = 23.34			
	Boolean values : true, false  
	return value : none

Type Casting : To change the type of variable.(If possible)
				Example -
						a = "123"		b = 31
						a = int(a)		b = str(b)
						print(a+5)		print(b + "ab")
						Ans = 128		Ans = 31ab

Input : It takes the input from user. (Its type is always string)
		Example - 
				a = input("Enter your name : ")
				print(a)
				print(type(a)) <- Always a string...
				
----------In Python index value starts with 0 --------------

Ascii code : earlier systems were using 8 bit for storing data that means only upto maximum 256 bits can be use to store values, which can only store some aplhabets and numbers. So this fails in modern days.
Unicode : now unicode has came which has 16 bits and this can store any aplhabets, numbers, emojis, any language letters.

In python specifically, string are a sequence of unicode charaters.

string advance eg : s = ' hi , this is "Arbaz" form \'pune\' '
			s = " hi , this is \"Arbaz\" form 'pune' "
			
	In python strings are immutable i.e once the strings are created it cannot be changed.
	
In string below operators only works:

Arithmetric : print('arbaz' + 'khan')  print('arbaz' * 5) ......Only + and * are allowed.
logical : python represent empty string as False and not empty string as True. i.e print('' and 'arbaz') will return ''
			
Sting slicing:
				name = "Arbaz"
				print(name[1])   -> Ans : r 
				print(name[-1])  -> Ans : z : this is helpful when you don't know the length of string and you need last element.
				print(name[0:3])   -> Ans : Arb  # O se lekar 3 tak..Excluding 3
				print(name[1:4])   -> Ans : rba  # 1 se lekar 4 tak..Excluding 4
				print(name[:5])   #Same as name[0:5] -> Ans : Arbaz
				print(type(a)) -> type = str
		Negative indices : 		A r b a z
								0 1 2 3 4      Length = 5
								-5-4-3-2-1
				print(name[-4:-1])   #Same as name[1:5] -> Ans : rbaz				
		Skip value in slicing:
								print(name[0:5:2]) #last value will print each 2nd letter.
								
		
		In Python, strings are immutable, which means you cannot directly modify or delete individual characters within a string. 

List: index value starts from 0 
		List are same as arrays in python i.e arrays in C and same is list in python. 
		But arrays are static and lists are dynamic. 
		Arrays are homogeneous and lists are heterogenuous here. 
		But, list takes more time and more space than arrays.
		Here, data is stored at different memory location and in list memory adderesses of this data are stored sequentially.
		Weird thing, python can also store any objects. i.e l = [1, 2, print, type, input]
		a = [1, 2, 3, 4, 5]
		c = [1,1.2,"qwerty",False] - > we can create list of different data types.
		a.append(6) -> appending use to add only 1 item
		a.extend([6,7,8]) -> use to add multiple items.
		a.insert(indexposition, newitem) - can add new item into desired location
		
		deleting item from list using index position : del a or del a[1]
		remove item from list using item : a.remove(2)
		pop -> a.pop() will delete last item. if a.pop(1) will delete with index.
		clear -> will clear the list and make list as empty list -> a.clear()
		
		We can also do slicing in list. - > print(c[0:3])
		
		print(type(a)) -> type = list
		
		Charaterstic:
						- Ordered i.e a=[1,2,3] is different from b=[3,2,1]
						- Can have a duplicate item.
						- can be nested
						- mutable i.e we can update the items in list -> b[1] = 4 or b[1:2] = [33,44]
						
		In list below operators only works:

		Arithmetric : print(a + b) print('arbaz' * 5) ......Only + and * are allowed.
		membership operator : in and not in -> 3 in list
		
		List function : 
						len, min, max, sorted, count, index, reverse, sort(this will be permenent), copy

Tuples: A tuple is an immutable data type in python i.e after assignment we cannot change the values of tupples. That means the methods such as adding, appending is not allowed.		
		t = (1,2,3,45,55)
		a = (1,) -> if only single element in tuple, we add comma at the end.
		a.count(1) : it will return number of times 1 appear in a.
		a.index(1) : it will return index of first occurence of 1 in a.
		print(type(t)) - > class = tuple
		
		In Python, tuples are immutable, which means you cannot modify them once they are created. 
		Therefore, you cannot delete elements from a tuple or modify the existing tuple directly. 
		However, you can create a new tuple with the desired elements.
		
		Same operations i.e arithmetric and membership can be performed.
		
		Zipping tuples :
							a = (1,2,3,4)
							b = (5,6,7,8)
							
							tuple(zip(a,b)) -> this will give ((1,5),(2,6),(3,7),(4,8)).....We can also apply for List i.e list(zip(a,b))
		
	Tuple unpacking : 
						- We can store values of tuple in variables. (Only thing is LHS variable should be equal to RHS tuple items)
							a,b,c = (1,2,3)
							print (a,b,c)...this will give 1 2 3
							
							If there are more values in RHS tuple, but we need only fewer
							a,b,*others = (1,2,3,4)
							print(a,b)   -> 1 2
							print(others)  -> [3, 4]
							
						- Values swaping :
							a =1
							b =2
							a,b = b,a     -> this implicitly create tuple on RHS and its same as a,b = (b,a)
							print(a,b)...this will swap values of a and b...
							
							In the line a, b = b, a, a tuple is indeed created on the right side with the values of b and a, but the unpacking syntax allows these values to be assigned to the variables a and b. 
							It's a concise way to swap the values without using a temporary variable. To break it down further:
							On the right side of the assignment, (b, a) creates a tuple with the values of b and a. This tuple is (2, 1) at the moment of assignment.
							The tuple (2, 1) is then unpacked, and its elements are assigned to the variables on the left side of the assignment. So, effectively, a is assigned the value of the first element (2), and b is assigned the value of the second element (1).
		
		
Main difference between Lists and Tuples :

	Syntax : For list we use [] and for Tuple we use ()
	Mutability : List are mutable whereas Tuples are immutable.
	speed : Generally Tuples are faster than list because of mutability.
	Memory : Tuples takes less memory than List.
	Built-in function : List has more functions than Tuple.
	Error prone : Bcz of mutability, List are error prone than Tuple.
			List :	a = [1,2,3] 
					b = a
					a.append(4)
					print(a)
					print(b)   ..... Here b will be also changing but we never appended any value to b. To avoid this we can use copy function of list.
			Tuple : a = (1,2,3)
					b = a
					a = a + (4,)
					print(a)
					print(b) ....here a and b will be having different values
	Usability : Any application where it is read only then we have to implement tuple, if want read and write we will be using List.
					
		
Dictionay: It  is a collection of key-value pairs. it is unordered, mutable, cannot duplicate keys.
			Syntax :
					MyDict = {
								"apple": "fruit",
								"criket": "game",
								"marks_list": [1,44,55],
								"tuple": (33,),
								"mydict2": {
												"pen": "paper"
											}
							  }
							  
					print(MyDict['apple'])	
					print(MyDict["marks_list"])
					print(MyDict['mydict2']['pen'])
				
				print(type(MyDict)) - > class = dict
				
		Adding : 
					myDict['newkey'] = 'yes'
					
		deleting :
					d.pop('newkey')
					del d['aa']
					d.clear()
				
	*****Important*********	
		If we are searching values which are not present in dictionay below are the two cases:
		
			print(MyDict.get('apple2')) -> Returns "none" as apple2 is not present in the dictionay
			
			print(MyDict['apple2']) -> Returns Error as apple2 is not present in the dictionay


Set : It is a collecction of non repitative(unique,no duplicates) elements.
		It is unordered( i.e the order in which we have added items will be not fixed, internally it will changed acc to hashing) and mutable. We can remove or add.
		Its specifically used to perform mathematical operation like union, intersection, symmetric difference, etc.
		The special feature is, Set itself is mutable but it can't contain mutable data types.(e.g. set inside a set is not allowed)
		
		As the sets are unordered, we can't do indexing i.e a[1]...we cannot fetch value using index. Also we cannot update values inside set.
		We can only add and delete items.
		For adding 1 item : a = {1,2,3}
							a.add(4) -> a = {1,2,3,4}
		For adding multiple item : a.update([4,5,6]) -> a = {1,2,3,4,5,6}.......Its same like append and extend in list.

		For deleting :
						del function -> del s  -> will delete set. (del s[1] will not work as indexing not allowed)
						discard -> a.discard(4) -> if not found will not throw error
						remove -> a.remove(4) -> if not found will throw error
						pop -> a.pop() will delete 1 item randomly
						clear -> a.clear() will clear the set and show empty set.
		Don't intialize set like s = {}...this will by default consider as dict datatype.
		DO like this -> a = set()
		
		a = {1,2,3,45,5}

		print(type(a)) - > class = set
		
		a = {1,2,3,45,5,1}
		
		print(a) -> {1,2,3,45,5} - > it will not print/store repitative elements.
		
		b = {}   -> if we create empty set like this. It will act as empty dictionary with type dict.
		An empty set can be created using below syntax:
		
			b = set()
			print(type(b)) -> class set.
			
	Set operations :
							s1 = {1,2,3,4,5}
							s2 = {4,5,6,7,8}
		Union (|) :
						s1 | s2 -> will print all items of both sets 
						
		Intersection (&) :
							s1 & s2 -> will print common items from both sets
		Difference (-) :
							s1 - s2 -> will print items of S1 which are not present in S2
		Symmetric Difference (^) : 
									s1 ^ S2 -> will print all items except the comman items.

	Set functions :
	
		len, sum, min, max, sorted
		s1.union(s2)
		s1.intersection(s2)
		s1.difference(s2)
		s1.symmetric_difference(s2)
		
		s1.isdisjoint(s2) -> will print true if both sets does not have same elements and false if have somthing in comman.
		s1.issubset(s2) -> boolean value
		s1.issuperset(s2) -> boolean value
		
		s1 = {1,2,3,4}
		s2 = s1.copy()
		
	Frozenset :
				frozenset set is just an immutable version of a python set object.
				fs = frozenset([1,2,3])
				
				All set operations will work here.
				All read function will work
				All write function will not work.
				
			
if-elif :  If else if statements.
			Syntax:
					if(a>3):
						print("hi")
					elif(a==7):
						print("here")    
					else:
						print("you")
			
					if(a>3):
						print("this")
Operators:

	Arithmetric operators: 
							+, -, *, / -> division, // -> integer division (i.e if the answer will be rouded off to an integer), % -> modulus (i.e it will divide and give you the remainder as answer), ** -> power-of operator ( i.e 5**2 is same as we write 5 raised to 2)
	
	Relational Operators:
							> , < , !=
							==  -> equals to
							>=  -> greater than equal to
							<=  -> less than equal to
	Logical operators:
						and -> True True = True O.W False
						or -> False False = False O.W True
						not -> True will be false and False will be true.
						
	Bitwise operator: 
						& -> bitwise and 
						| -> bitwise or
						~ -> bitwise not 
						^ -> bitwise XOR - exclusive OR - 1 1 = 0 , 0 0 = 0 , 1 0 = 1 , 0 1 = 1
						<< -> bitwise left shift( adding 0 to left) : 0101 -> 1010 
						>> -> bitwise right shift ( adding 0 to right and removing any from left) : 0101 -> 0010
						
	Memembership operators: 
							in / not in -> it use for finding any in string, tuple, dict
							
						
While Loop : Syntax:

			i = 10

			while(i>0):
				print("Yes" + str(i))
				i = i - 1
				
	You can also add else statement in while loop :
	
			else:
				print("limit crossed")
				
				
For loop :  Syntax:
			l = [1,2,3,4,5,6,7,8,9]

			for i in l:                      
				print("Yes" + str(i))
				
		In range format:
			for i in range(8):  -> range can have various values like : range(start, stop, step-size)
			print(i)
			
			for i in range(2, 11, 2):      #range(start, stop, step-size)  
			print(i)
			
		For loop with else:
			In for loop else statement will execute once for loop is exhausted.
			
			for i in range(8):
				print(i)
			else:
				print("end")
				
		break/continue statement:
		
			for i in range(8):
				print(i)
				if i == 3:
					break   (continue  -> it will exit current loop task and go for parrent loop task.)
					
		Pass statement :
			
			pass keyword is same as "do nothing"
			
Funtions: It is a block of code which we can reuse in future programming.
			Syntax : def funct():
						//write reusable code here
						return() -> if function need to send any values at that line where function is call.
			Types of Functions:
				Built-in Function : Already define in python eg: print(), len(), range()
				User-define Function : Defined by user eg: funct1()
			
			When the function is called, the values inside () is called arguments and where function code runs its called parameter. In simple words arguments bacisally a value given to a parameter.
			
			Function with arguments: funct(marks, arg2, arg3):	-> here marks is argument		
			
			Default parameter value: We can set default arguments in function like below(it is used when no arguments are passed):
				funct1(name="Arbaz"):
				
			Keyword parameter :
			 funct1(b=3, a=2)....it is used when we don't know the position of parameter.
			 
	*args and **kwargs :
						They both are special Python keywords that are used to pass the variable length of arguments to a function.
						If we are having dynamic parameters i.e user can add any parameters to a functions that time we use this.
						Remember order is important : (normal -> *args, **kwargs)
						The words args and kwargs are only a convention, you can use any name of your choice.
					*args :
							Allows us to pass a variable number of non-keyword arguments to a function.
							def func(*args):
								prod = 1
								
								for i in args:
									product = product * i
									
							return product
							
							func(1,2,3) .... we can now add multiple arguments here.
							
							Always remember *args takes arguments and store it in tuple. You can check by printing args.
							
					**kwargs :
								Allows us to pass any number of keyword arguments.
								Its basically used to pass the dictionay key-value pair items to a function.
							e.g. 
									def display(**kwargs):
										
											for(key,value) in kwargs.items():
												print(key,'->',value)
									
										display(india='delhi')
										
	*** Important : A function always returns something! how-> In some function we explicity return the value. at that time it will return value. If we don't add return keyword in function. It will implicitly return None.
	
	Nested function:
						A function inside a function.
						Its a very interesting way to hide the function from calling by main body as the inside function can be only called by its outer function.
						
	Function are the 1st class citizens in python. i.e You can use functions as a datatype.
			- You can store the function in a variable.
				def func():
					'''
					
				x = func
				
			- You can delete function
				del func()
				
			- You can store function into list.
				L = [1,2,3,func]
				
			- You can also pass function as a argument
				funcb(a,func())
			
			- You can pass function as return value. Two cases : 1. return function can be of other.    2. function calling itself like below.
				
			Recursion function : Function calls itself.
			
				def funct1(n):
					if n == 0 or n == 1:     -> Base condition which doesn't call function any further.
						return 1
					else
						return n*funct1(n-1)   -> function calling itself.
				
Common in-built functions:		(note : all below function does not change the original variable. It will create another variable)

		len(), max(), min(), sorted('arbaz'),
		s = 'hello world'
		s.capitalize() -> Hello world
		s.title() -> Hello World
		s.upper() -> HELLO World
		s.lower() -> hello world.
		s.count('l') -> 3
		s.find('e') -> 1
		s.endswith('s') -> false
		s.startswith('h') -> true
		s.isalnum -> will check if string contains alpha numeric.
		s.isdigit -> will check is digit
		s.isidentifier -> will check if string can be a identifier.
		s.split() -> will split the string and store it in list. -> ['hello', 'world'] -> when split() it will split acc to space and if pass something in bracket it will split from that X.
		" ".join(['hello', 'world']) -> will join the list with the space if " ". if "-" it will add - between two words.
		s.replace('world', 'boy') -> will replace world with boy.
		s.strip() -> will remove all spaces from string.
		
					
Files : Files is the data stored in a storage device. A pyhton file can read or write file content.
		Types : 
			Text File : (.txt, .c, etc)
			Binary file : (.jpg, .dat, etc)
			
		There are different function to handle file.
		
		Steps to handle file : Open file -> read/write -> close file
			Opeining File : file = open("sample.txt", "r")  -> By default file is opned in read mode.
				Modes of opening file :
					r : Open for reading    ( "rb" : for reading binary file ; "rt" : for reading text file.
					w : Open for writing	( If file not present, it will create a file) (If present, it will erase all data and overwrite current data.)
					a : Open for apending	( It will continue updating file from end of data in file.)
					+ : Open for updating
			closing File : file.close()
			
			Reading file : data = file.read() - will read full file
					Multiple ways:
							data = file.read(2) - will read 2 characters form file.
							data = file.readline() - will read 1 line form file. If need another line add this code again.
							
			Writing in file : file.write("This is written in write mode of python")  This can be written in multiple times.
			
		Best way to handle file is using with statement ->
		
															with open('sample.txt', 'r') as file:
																data = file.read()
																print(data)
																						-> This does not require close function, as it is done automatically
																						

Modules :
			Modules are simply the reusable code which we import in our programs. Its same as libraries in C.
	Some of the modules are : 
								math -> can perform all mathematical operations.
								keyword -> can see all the keywords.
								random -> can get any random numbers.
								datetime -> can get date and time.
								If we want to search what are the modules present in our pc, command help('modules')
			

OOPs Concepts :	Object oriented programming is a way that is used for efficiency and non repitative.
				In this way we will create an object to solve the problem.
			
			Class : It is a blueprint for creating objects.
					Syntax : 
								class Employee:				-> class name is written in Pascalcase(i.e first letter caps)
									#variables
									#methods/functions
			Object : It is an instance of class. 
						Memory is allocated only after an object is defined.
						Abstractions/Encapsulation : Object of given class can invoke the methods available to it without revealing the implementation details to users. 
						Syntax : 	
									user1 = Employee()
									
									...Basically an object code is only 'Employee()'. we are storing the location of this object in user1 
									
				Modelling a problem :
										Noun : class -> Employee
										Adjective : Attributes -> name, age, salary
										Verb : Methods -> getSalary(), increment()
										
			Class Attributes : The attributes that belongs to class rather than any particular object.
						Example:
									class Employee:
										company = "Google"   ----> ( Attributes specific to each class)
										 
									user1 = Employee()       ----> (Object Instantiation)
									print(user1.company)
									Employee.company = "Microsoft" -> (Changing class attibutes)
									
			Instance Attributes : The attributes which belongs to the object(instance)
								
									example : continuing  above
												user1.company = "youtube"
								Instance attribute take preference over class attributes.

			'Self' parameter : self refers to instance of an class. It is automatically passed with the function call from an object.
								Example : 
											harry.getSalary()   ---> here self is harry
											Above is equivalent to ->  Employee.getsalary(harry)
											
					The function in class is define as : 
															class Employee:
																company = 'Google'
																def getSalary(self):
																	print("salary is 100k")
							
					Always remember : function outside the class is called function. but the function inside the class is called as method.
							
					Two types of methods : static method and intance method.
					
					Static method : sometimes we need the function which does not use self parameter, we can define a static parameter like this:
							 A static method is a method that belongs to the class rather than an instance of the class.It can be called on the class itself, without creating an instance of the class.			
											@staticmethod
											def getsalary():
												print("salary is 100k")
												
			__init__() Constructor : Its a magic method/function a.k.a. dunder method.
				(dunder method)		It is the special method which is first run as soon as the object is created. We don't need to call this method
											__init__() method is also called as constructor
											It  takes the self argument and also takes other arguments.
										For example:
													class Employee:
														def __init__(self,name):
															self.name = name
														def getsalary(self):
															...
															
													harry = Employee("arbaz")   -> object can be instantiated using the constructor like this.
													
									The real example of constructor is : unlike other methods which are dependent on users response, constructor is not dependenton users response. it depends on program itself. i.e when the program starts it will be executed.
																			Its real life use is : to add all logic of configuration of program which are needed when the program starts (for e.g internet releted config, location, space related)
													
			Inheritance : It is a way of creating a new class from an exiting class.
						Syntax : 
								class Employee:     -> Base class/ parent class
									#code
									....
									
								class Programmer(Employee):     -> derived class/ child class
									#code
									....
									
							We can use methods and attributes of Employee in programmer object.
							Also, we can overwrite or add new attributes and methods in programmer class.
							
							
					Types of Inheritance : 
						1. Single Inheritance : It occurs when child class inherits only one parent class.
											Base -> derived
						2. Multiple Inheritance : More than one parent class.
											parent1			parent2
												|				|
												\_______________/
														|
													  Child
									Syntax :
											class Employee:     -> Base class/ parent class
												#code
												
											class Company:     -> Base class/ parent class
												#code
												
											class Programmer(Employee,Company):     -> derived class/ child class
												#code
												
									Here if there is same method/attribute in both parents, child instance will take preference of first class written in child {} parenthesis over second.
						3. Multilevel Inheritance : When child class becomes the parent of another child class.		
							
					Super() method :
								super method is used to access the methods of super/parent class in derived class.  Mostly used for __init__ function calling
								
								E.g :   class Employee:
											def __init__()
											
										class programmer(Employee):
											super().__init__()       -> can access method of parent class.
											
											def method():
												code
												
					class methods :
									Class method is a method which is bound to class and not an object of class.
									@classmethod decorator is used to create a class method
									Syntax :
												@classmethod
												def change( cls, p1, p2):     -> instead of self we use cls here.
														......
														
					Getters and Setters : 
											These are the decorators which are used to dynamically modify the attributes in class.
								1. Getter uses @property decorater to create dynamic attributes. 
										If we need to set the attribute on the base of above predefine attribute, we uses this decorator. 
										@property decorator is used above function of which we want dynamic variable
									example:	
										class Employee:
											Company = 'Google'
											YearlySalary = 400000
											Yearbonus = 100000
											#If we need total salary to be dynamic, in this case it should be yearly sal + bonus; we uses getter i.e @property decorator

											@property
											def TotalSalary(self):
												return self.YearlySalary + self.Yearbonus
												
										e = Employee()
										print (e.TotalSalary)
										
								2. Setter : It is used to change value of already defined attributes in class.
										Continuing above example, if we need to change Yearbonus base on total salary,
											In class, we will add function and setter decorator,											
												@TotalSalary.setter
												def TotalSalary(self, TotalSalary):
													self.Yearbonus = TotalSalary - self.YearlySalary
											e = Employee()
											print (e.TotalSalary)
											#setter to set Yearbonus
											e.TotalSalary = 600000
											print(e.Yearbonus)   
					
					Operator overloading : Operator in python can be overloaded using dunder methods.
											These methods are called when a given operator is used on the objects.
											
									Operators can be overloaded using the below dunder methods,
												p1 + p2			->			p1.__add__(p2)
											like this, *  -> __mul__    ;   -  -> __sub__  ; /  -> __truediv__
											
Exception handling : There are many build-in exceptions which are raised in python when something goes wrong.
					Exception in python can be handled can be handled using a try statement. The code that handles the exception is written in except clause.
					Example:
								try:
									#code						-> code which might throw error.
								except Exception as e:
									print(e)
					When the exception is handled, the code flows continues without program interuptions.
					
					There are many standard error exceptions in python for which we can implicitly add custom error text.
					e.g: except ZeroDivisionError:
						 except TypeError:
						 except:     -> all other error are handled here.
						 
					We can raise custom exceptions using raise keyword.
					e.g :	try:
								#code
							except:
								raise ValueError("This is wrong")
								
					try with else clause:
						Sometimes we want to run a piece of code when try was successful.
					e.g :	try:
								#code
							except:
								raise ValueError("This is wrong")
							else:
								#code 				-> This will run only if try was successful and it doesn't go to except block.
								
					try with finally:
						Pythons offers a finally clause which ensures execution of a pice of code irrespective of the exception.
					e.g :	try:
								#code
							except:
								raise ValueError("This is wrong")
								exit()
							finally:
								#code 				-> This will always run irrespective to any exit method written in except clause. thia is mainly use to close any in progress file, or add some closing code before exiting.

if __name__ == '__main__' in python :
								__name__ evaulates to the name of the module in python from where the python program is ran.
								
								If the module is being directly run from command line, the __name__is set to string '__main__'. 
								Thus this behaviour is used to check whether the module is run directly or imported to another file.
								It is use when : let say if we have to import first block of code from file1 to 2nd file. while importing we have to give full file name( not that block). While in 2nd file full code run.
								In this case if we write above code to the part for which we don't need to export, only first block will run in 2nd file.
								
Global keyword : It is used to modify the variable outside of the current scope.
				Syntax : global attributeName
				In method/function if we need to access attribut which is outside of funtion, we use global keyword.
				
				
Enumerator function in python : The enumerator function adds counter to an iterable and returns it
				example :
							for i,item in list:
								print(i,item)     -> prints the items of the list with index.
								
List comprehensions:
			It is an elegant way to create lists.
			newlist = [ expression for item in iterable if condition == true]
			- More time-efficient and space-efficient than loops.
			- Require fewer lines of code.
			- Transforms iterative statement into a formula.
			example:
						list1 = [1, 3, 5, 55, 77, 21, 87, 90, 786, 5436]
					If we have to we are create list2 which will store number greater than 70 , we can do like below,

						list2 = [i for item in list1 if item > 70]
						
Lambda function: Its a small anonymous Function created using an expression using lambda keyword.
				Syntax :
							funcnName = lambda arguments: expressions    -> can be used as normal function.
				example:
							square = lambda x: X*X
							square(6)    ---> return 36
							
							sum = lambda a, b, c: a+b+c
							sum(1, 2, 3)   ----> return 6
		diff between lamda and normal function :
						No name to function.( we only use keyword lamda)
						lamda has no return value. (i.e it will return a function itself instead on none)
						lamda is written in 1 line
						not reusable
							
join function: It makes the sentence of words present in list/ tupple.
								E.g. :
										l = ["apple","mango","peer"]
										
										sentence = " and ".join(l)
										
										print(sentence) 		-> prints apple and mango and peer
										
format function : Currently we have "f" function in string to add any variable value. Earliear(python 3.5) we were having format function. It formats the value inside the string into a desire output.
						e.g :
								name = 'Arbaz'
								a = " This is {}".format(name)
		If we have more that one argument : a = " This is {} from {}".format(name, state)
		If we have have to specify argument location(argument index starts from 0) : a = " This is {0} from {1}".format(name, state)
		
Map, filter and reduce: 
						Map applies the function to all the item in the input list	
								print(list(map(function, input_list)))
								
						filter create the list of items for which the function returns true.
								print(list(map(function, input_list)))
								
						Reduce applies a rolling computation to sequential pair of elements.
								from functools import reduce
								val = reduce(function, list1)
								
								If the function computes sum of 2 numbers and the list is [1,2,3,4]
									It will do sum like (((1+2)+3)+4) and print. its called sequential computation.
						
Virtual Environment: An environment which is same as system interpreter but is isolated from other python environment on the system.

			Installation: At the very begining, we need to install package i.e below
							
							pip install virtualenv
							
						We create a new environment by below syntax in terminal.
						
							virtualenv myprojectenv
							
						Next step after creating a new environment is to activate it.
							
								.\myprojectenv\Scripts\activate.ps1
								 To deactivate the environment we simply write - deactivate
						We can now use this virtual environment as a seperate python installation. 
						
			By "pip freeze" command we can see the packages installed in virtual env.
				To save the content of pakages we write : pip freeze > requirement.txt ---->>> by this way we can send the details of pakages installed in our virtual system to anyone. They can recreate the same envireonment which we are using.
				
			To install packages from requirement.txt, command is pip install -r requirement.txt
					
DS Algo Python: 

Data structure : It is a way to store and organized data efficiently.
				Need : In Programming there are some problems which are difficult to solve. It can be efficiently solved using DS.
				
	Two Types : Linear and Non Linear
	
	Linear : Array, Linked list, Stacks, Queue, Hashing
	Non Liner : Trees, Graphs
	
	Arrays : It is Linear data structure which is used to store multiple items of same type in continues memory location.
			Disadvantage : 1. Fixed size (Memory Wastage)
						   2. Homogenuous (different types can't be store)(lack of flexibility)
						   
		Lists are the referencial array i.e lists stores the addresses of heterogenuous data in sequential manner.