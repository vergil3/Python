#python exercise variables, print, input etc
welcomeText = "Hello "
print(welcomeText)

#checking Knowledge
enteredName = input('Please enter your name: ')

if enteredName == 'luk':
	print('Hello %s' %enteredName)
else: print('wrong name!')

#how to declare a variable with no value
x = None
if 0:
	x = 1
if x != None:
	print(x)

#how to delete none used variables
x = 3
del x
print(x)
	NameError: name 'x' is not defined