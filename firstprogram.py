def intro():
	print("Daniel Castro")
	number = input("Place a number\n")
	print(number)

def dataTypes(): 
	"Python Interpreter decides the data type"
	print("Data Types - Fundamental \n")
	print("INTS AND FLOATS")
	int
	print("1 + 3")
	print(type(1+3))
	"Power: 2 ^3"
	print(2 ** 3)
	"double divide return integer"
	print(5 // 3)
	"Module 5 /4 has 1 left"
	print(5%4)
	float
	print(12.12+1.99)
	"Math Functions"
	round(3.1)
	abs(-9) 

	"Other Data types"
	print("BOOLEANS")
	bool 
	boolean = True  
	print("*" * 6)

	str
	print("STRINGS")
	long_string = """
	WOW
	O O
	WOW
	"""
	print(long_string)
	print("Hello" + " Daniel")
	"Convert Variable Types "
	print("Number : " + str(100) )
	"Escape sequence"
	print("\t Hello")

	"formatted strings "
	name = "Daniel"
	age = 20
	"name[0] D Strings can't be changed"
	"name[0:3] Dan"
	"name[-1] l"
	print(f"Hi {name}. You are {age}")
	len(name)

	print("LISTS")
	list
	li = [1, "2",3,True,5,6,7,8,"9",10]
	print(li)
	print(li[2:9:2])
	li[0] = 11
	new_li = li
	print(new_li)
	len(li)
	"Add operations"
	li.append(100)
	li.insert(111, 4)
	"Remove Operations "
	li.pop(0)
	li.remove(8)
	# li.clear()
	li.count(6)
	# li.sort() in homogeneous lists only it modifies actual list
	# sorted(li) creates new list
	li.reverse()   
	print(li)
	li.index("9")
	"create list from 1 to 100"
	list(range(1,100))
	sentence = ""
	new_sentence = sentence.join(["hi", "my"])
	print(new_sentence)
	"Unpacking "
	a,b,c, *other = [1,2,3,4,5,6,7,8,9]
	"Other contains 4 and beyond"
	print(other)
	print("Matrix")
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	print(matrix[0][1])

	print("TUPLES ")
	tuple
	"Can't be changed, lists can be changed"
	my_tuple= (1,2,3,4,5)
	a,b, *other = (1,2,3,4,5)
	my_tuple[2]
	new_tuple = my_tuple[1:4]

	print("SETS")
	set
	"Unordered collection unique elements"
	my_set = {1,2,3,4,5}
	my_set.add(100)
	"Not added already there"
	my_set.add(2)
	1 in my_set
	len(my_set)
	new_set = my_set.copy()
	".difference takes different elements between sets "
	" difference_update deletes difference and adds othe"
	" union creates new set with all elements"
	" intersection "
	"issubset true or false"
	"issuperset"

	print("DICTIONARIES")
	dict
	"Unordered key value pair"
	"key must be inmutable"
	dictionary = {
		'a':[1,2,3,4],
		123:20,
		True: True,
		'b':100
	}
	print(dictionary['b'])
	"Avoid error of not finding key"
	dictionary.get(101)
	"basket" in dictionary.values()
	20 in dictionary.keys()
	"See all items in dictionary"
	dictionary.items()
	dictionary.pop("b")
	"If not exists it creates"
	dictionary.update({'new_key': 100})
	dictionary.clear()


	None 
	"Like NULL in other Programming Languages" 
	

	"For complex numbers imaginary"
	complex

	print("EXTRA")
	"variables to store information"
	number_print = "100"
	a,b,c = 1,2,3
	_private_variable = 100
	CONSTANT_PI = 3.14
	"__ starting are untouchable variables don't name them like that"
	print("The number in string data type is " + number_print)
	"Augmented assignment"
	a += 2;
	print("Data Types - Custom Classes \n")
	print("Data Types - Specialized  \n")

def other_basics():
	print("COnditional Logic")
	x = 100
	if x == 0 and x==1:
		print("if")
	elif False: 
		print("elif")
	else:
		print("else")

	#truthy falsy convert to boolean 
	True is 1 # checks if same in memory
	True == 1 # converts to bool 1 

	# loops also [1,2,3,4] or (1,2,3,4) 
	for item in "Zero":
		print(item)
	#iterable - list, dictionary, tuple, set , string
	user = {
		"name": "Golem",
		"age": 10
	}
	for key, value in user.items():
		print(key , value )

	for _ in range(0,10,2):
		print(_)

	for i, char in enumerate("Hello"):
		print(i , char)

	i = 0
	while i < 5:
		print(i)
		i = i + 1
	# break = exit loop
	# continue: goes top loop
	# pass does nothing

	# default parameters 
	def say_something(text="None" , other="Nothing"):
		# shows the information 
		"""
		Info: this prints a text
		"""
		print(f"Hiiiii {text}  {other}")
		return "completed"

	say_something("Daniel", "next")
	say_something()
	#*args Accept any number or arguments
	#**kwargs for dictionary num1 and num2 
	def super_func(*args, **kwargs):
		total = 0
		print(sum(args))
		for items in kwargs.values():
			total += items
		print(total)
	super_func(1,2,3,4,5, num1=5, num2=7)
	
#Classes 
class BigObject: 
	#Class Object Attribute is static
	membership = True

	#Constructor
	def __init__(self, name="None", age=0):
		self._name = name
		self._age = age

	#method
	def run(self):
		print("run")
		return "done"

	def shout(self):
		print(f"name: {self._name}")

	# method without instantiate
	#care about class state to create object 
	@classmethod
	def add(cls, num1,num2):
		return cls ("Da ", num1 +num2)

	#no care class state
	@staticmethod
	def add2(num1,num2):
		return num1 +num2

#inheritance from BigObject has all 
# from BigObject  
class superBigObject(BigObject):
	#Constructor
	def __init__(self, name="None", age=0 ,size=0):
		BigObject.__init__(self,name,age)
		self._size = size

	def shout(self):
		# apply both shout methods parent and own
		BigObject.shout(self)
		print(f"name of SuperBIg: {self._name}")

#Multiple inheritance possible
"""
class multipleInheritance(user1, user2):
	def __init__(self, name, age ,size):
		user1.__init__(self,name,age)
		user2.__init__(self,name,size)
"""
def use_class():
	# Uses class method to create class 
	player3 = BigObject.add(2,3)
	print(player3._age)

	obj1 = BigObject("Daniel",20)
	print(obj1._name)
	print(BigObject.add2(1,2))
	#just this object has this attribute
	obj1.attack = 50
	# check OOP encapsulation, abstraction, 
	# inheritance and polimorpfism
	superObj1 = superBigObject("Daniel", 12, 12)

	superObj1.shout()
	print(superObj1._age)


def functionalProgramming():
	# no side effects "touch outside function
	# no print and no variables outside "mantain as possible"
	# does one thing 
	def multiply_by2(li):
		new_list = []
		for item in li: 
			new_list.append(item*2)
		return new_list

	def multiply_by2Map(item):
		return item*2

	#1°param = function to use, 2° array elements
	print(list(map(multiply_by2Map, [1,2,3])))
	# print([1,2,3].map(multiply_by2Map)

	def only_odd(item):
		return item % 2 != 0
	#function for criteria 2° list or array
	print(list(filter(only_odd, [1,2,3])))

	#adds elements in tuple
	print(list(zip([1,2,3], [10,20,30])))
	from functools import reduce
	
	# 1° sumatory 2° each item list
	def accumulator(acc, item):
		return acc + item

	#reduce: reduce list to 1 item 
	# 1° function 2° list 3° starting point#
	print(reduce( accumulator,[1,2,3], 0))

	# lambda functios 
	#lambda param: action(param)
	# lambda variable: function
	print(list(map(lambda item: item*2, [1,2,3])))
	print(reduce(lambda acc , item: acc+item, [1,2,3] ))

	#comprehensions used in list, set , dictionary 
	#list comprehensinons
	my_list = [char for char in "hello"]
	my_list = [num*2 for num in range(0,10)]
	my_list = [num*2 for num in range(0,10) if num %2 == 0]
	print(my_list)
	#find duplicates 
	some_list = ['a','b','a']
	dup = list (set ( [x for x in some_list if some_list.count(x)>1] ))
	print("Duplicates")
	print (dup)
	#dictionary comprehension 
	simple_dict = {
		'a': 1,
		'b': 2
	}
	my_list = {char for char in "hello"}
	my_dict = {key:value**2 for key, value 
		in simple_dict.items() if value%2 == 0 }
	print(my_dict)

def decorators():
	# this is high order function 
	# it works with function anre returns function
	def hello(func):
		func()

	def greet():
		print("hey")

	a = hello(greet)

	print(a)

	#decorator supercharges function
	#in this case with "*********"
	def my_decorator(func):
		def wrap_func(*args,**kwargs):
			print("*******")
			func(*args, **kwargs )
			print("*******")
		return wrap_func

	@my_decorator
	def printHello(greeting, emoji=":("):
		print(greeting, emoji)

	printHello("Hellloooo")

	#decorators to see performance 
	from time import time
	def performance(fn):
		def wrapper(*args, **kwargs):
			t1 = time()
			result = fn(*args, **kwargs)
			t2 = time()
			print(f"took {t2-t1} s")
			return result
		return wrapper

	@performance
	def long_time():
		for i in range(10000000):
			i*5

	long_time()

def error_Handling():
	# several error handling only activates when
	# error type found 
	try:
		age = int(input("age?"))
		print(age)
		10/age
		#stop program to let user programmer know a problem
		raise ValueError("Hey stop")
	except ValueError as err :
		print(f"Enter Number {err}")
	except (ZeroDivisionError, TypeError) as err:
		print(f"Enter Number higher 0 {err}")
	else:
		print("thanks")
	finally:
		print("I am done")


#creates a list of something 
def generators():
	# faster gives 1 at a time 1 --> then 2 and so on
	range(100)
	# slower uses all #'s in memory'
	list(range(10))
	# 1 by 1 in memory our generator
	# just use yield keyworkd
	def generator_function(num):
		for i in range(num):
			yield i

	for item in generator_function(100):
		print(item)

	def fib(number):
		a= 0
		b = 1
		for i in range(number):
			yield a
			temp = a
			a = b
			b = temp + b

	for x in fib(100):
		print(x)


def fileInputOutput():
	my_file = open("test.txt")
	print(my_file.read())
	my_file.seek(0)
	print(my_file.read())
	my_file.seek(0)
	print(my_file.readline())

	my_file.close()
	# mode= "r+w" also to 
	# you can use a path
	with open("test.txt", mode="a") as my_file:
		text = my_file.write("Newline\n")

def regular_Expression():
	import re

	string = "search inside of this text please!"

	print("search" in string)
	pattern = re.compile("this")
	a = re.search("this", string)
	b = pattern.findall(string)

#works without the function 
# run several files of unittest with command:
# python -m unittest -v
def unit_test():
	import unittest
	#program with funtions to test
	import main 
	"""
	def do_stuff(num=0):
	try:
		if num:
			return int(num) + 5
		else:
			return "please enternumber"
		except ValueError as err: 
			return err
	"""

	class TestMain(unittest.TestCase):
		#before each function run this first
		def setUp(self):
			print("this first")

		def test_do_stuff(self):
			test_param = 10
			result = main.do_stuff(test_param)
			self.assertEqual(result,15)

		def test_do_stuff2(self):
			test_param = "dahdadh"
			result = main.do_stuff(test_param)
			self.assertIsInstance(result,ValueError)

		def test_do_stuff3(self):
			test_param = None
			result = main.do_stuff(test_param)
			self.assertEqual(result,"please enter number")

		def test_do_stuff4(self):
			test_param = ""
			result = main.do_stuff(test_param)
			self.assertEqual(result,"please enter number")

		def tearDown(self):
			print("clean up")

	unittest.main()

def ImageProcessing():
	from PIL import Image, ImageFilter

	img = Image.open("./pokedex/pikachu.jpg")
	#img.format .size .mode.
	print(img)
	#different filters 
	filtered_img = img.filter(ImageFilter.SMOOTH)
	filtered_img.save("blur.png", "png")
	# convert to other formats 
	filtered_img = img.convert("L")
	filtered_img.save("grey.png","png")
	filtered_img.show()
	# roatted image  resize 
	change_img = filtered_img.rotate(90)
	change_img = filtered_img.resize((300,300))
	change_img.save("rotate.png", "png")

	# exercise
	import sys 
	import os
	from PIL import Image

	image_folder = sys.argv[1]
	output_folder = sys.argv[2]

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	for filename in os.listdir(image_folder):
		img = Image.open(f"{image_folder}{filename}")
		clean_name = os.path.splitext(filename)[0]
		img.save(f"{output_folder}{clean_name}.png", "png")
		print("all done")

def pdf_processing():
	import PyPDF2
	# for pdfs read binary 
	with open("dummy.pdf", "rb") as file:
		reader = PyPDF2.PdfFileReader(file)
		# several attributes to get from page
		print(reader.numPages)
		# rotate check library
		page = reader.getPage(0)
		print(page.rotateCounterClockwise(90))
		writer = PyPDF2.PdfFileWriter()
		writer.addPage(page)
		with open("tilt.pdf", "wb") as new_file:
			writer.write(new_file)

def send_emails():
	import smtplib
	from email.Message import EmailMessage

	email = EmailMessage()
	email["from"] = "Pepe"
	email["to"] = "andrei@zero.io"
	email["subject"] = "You won 1000000 dollars"

	# you can add html pages to this 
	email.set_content("I am master")

	# this adjusted for each typecreates smtp server
	with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login("email@gmail.com", "password")
		smtp.send_message(email)
		print("send email")


def password_checker():
	import requests
	import hashlib
	import sys

	def request_api_data(query_char):
		url = "https://api.pwnedpasswords.com/range/" + query_char
		# get several hashes 
		res = requests.get(url)
		if res.status_code != 200:
			raise RuntimeError(f"Error fetching: {res.status_code}, check API try again")
		return res

	def get_password_leak_count(hashes, has_to_check):
		hashes = (line.split(":") for line in hashes.text.splitlines())
		for h, count in hashes:
			if h == has_to_check:
				return count
		return 0


	def pwned_api_check(password):
		sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
		print(sha1password)
		first5_char, tail = sha1password[:5], sha1password[5:]
		response = request_api_data(first5_char)
		print(response)
		return get_password_leak_count(response,tail)
	
	def main(args):
		for password in args:
			count = pwned_api_check(password)
			if count:
				print(f"{password} was found {count} times")
			else:
				print(f"{password} NOT found")
		return "done!"

	main(sys.argv[1:])


	# request_api_data("12345")
	# pwned_api_check("123")

def web_scraping():
	#download the html
	import requests
	# grab html and clean data 
	from bs4 import BeautifulSoup
	import pprint

	# place url to scrap
	res = requests.get("https://news.ycombinator.com/news")
	soup = BeautifulSoup(res.text, "html.parser")
	#show desired specific data
	#print(soup.body.contents)
	#print(soup.find_all("div"))
	# css selector
	links = soup.select(".storylink")
	subtext = soup.select(".subtext")

	#sort a dictionary 
	def sort_stories_by_votes(hnlist):
		return sorted(hnlist, key= lambda k: k["votes"], reverse=True)

	def create_custom_hn(links,subtext):
		hn = []
		
		for idx, item in enumerate(links):
			#grab title link and votes
			# title = links[idx].getText()
			# href = links[idx].get("href",None)
			title = item.getText()
			href = item.get("href",None)
			vote = subtext[idx].select(".score")
			# get only if they have votes 
			if len(vote):
				points = int(vote[0].getText().replace("points", ""))
				if points > 99:
					hn.append({"title": title, "link":href, "votes": points})
		return sort_stories_by_votes(hn)

	pprint.pprint(create_custom_hn(links, subtext))

#### import modules as example.py contains function method()
#### this is just a file 
#import example 
# example.method()

#### packages is in folder with exampleFolder.py
# import folder.exampleFolder 
#folder.exampleFolder.method("hello")

##### problem is collitions same name function in 2 packages
# from folder.subfolder.exampleFolder import method
# method()


# intro()
# dataTypes()
# other_basics()
# use_class()
# functionalProgramming()
# decorators()
# error_Handling()
# generators()
# fileInputOutput()
# regular_Expression()
# unit_test() delete the function to work 
# unit_test()
# ImageProcessing()
# pdf_processing()
# password_checker()
web_scraping()
