#random basics about python
'''comments in more than
 one row'''

 #how to print a variable on the screen:
stringToPrint = 'Hello String!'
print(stringToPrint)

#enter a name and print it:
#inputYourName = None
inputYourName = input("Enter your name: ")
print(inputYourName)

#how does an if work:
a = 10
b = 12
c = input('Enter a number:')

if a > b:
	print("A is bigger than B")
elif a < b:
	print("B is bigger than A")
elif a > c:
	print("A is bigger than C")
elif a < c:
	print("C is bigger than A")