import turtle
#Fahrenheit to Celcius function
def FToC(F):
	if F == str('Program Startup'):
		startprogram()
	try:
		C = (float(F) - 32) * 5/9
		print(F,'Degrees Fahrenheit is equal to',C,'Degrees Celsius.')
		startprogram()
	except:
		print("Please enter a real number.")
		FToC(input("How many Degrees Fahrenheit would you like to convert into Degrees Celsius?"))
#Acres to barns function
def AToB(A):
	if A == str('Program Startup'):
		startprogram()
	try:
		B = float(A)*4.047*10.0**31.0
		print('There are about',B,'Barns in',A,'Acres.')
		startprogram()
	except:
		print("Please enter a real number.")
		AToB(input("How many Acres would you like to convert into Barns?"))
#Polygon draw tool
def Polygon(N):
		try:
			N = int(N)
			if N < 1:
				print("I'm stopping you right there...")
				startprogram()
			a = 180-(((N-2)*180)/N)
			L = 500/N
		except:
			print('\nPlease enter an integer.')
			startprogram()
		try:
			polygon=turtle.Turtle()
			print('Drawing in annother window...')
			for x in range(0, N):
				polygon.forward(L)
				polygon.left(a)
			print('Success! Your Polygon has been drawn in annother window.')
			startprogram()
		except:
			print('Sorry, something went wrong. Did you close the drawing window?')
			startprogram()
def Closer():
	print('Closing Program...')
def startprogram():
	print('\nWelcome to Program Start. The avalable programs are currently Program Startup, Fahrenheit To Celsius(1),\nAcres To Barns(2), Draw A Regular Polygon(3), and Close\n')
	run = str(input("Please type the name of one of the Embedded Programs listed above that you would like to Run."))
	print('Starting',run)
	if run == str('Fahrenheit To Celsius'):
		print('Done.\n')
		FToC(input("How many Degrees Fahrenheit would you like to convert into Degrees Celsius?"))
	if run == str('1'):
		print('Done.\n')
		FToC(input("How many Degrees Fahrenheit would you like to convert into Degrees Celsius?"))
	if run == str('2'):
		print('Done.\n')
		AToB(input('How many Acres would you like to convert into Barns?'))
	if run == str('Acres To Barns'):
		print('Done.\n')
		AToB(input('How many Acres would you like to convert into Barns?'))
	if run == str('3'):
		print('Done.\n')
		Polygon(input('How many Sides would you like your Polygon to have?'))
	if run == str('Draw A Regular Polygon'):
		print('Done.\n')
		Polygon(input('How many Sides would you like your Polygon to have?'))
	if run == str('Close'):
		Closer()
	else:
		print('Startup Failure, troubleshooting...\n')
		print('Invalid Input, check that your spelling and capitalization are the same as mine.\n')
		print('Tip: you can also use the number beside the name of a program to run it.')
		startprogram()

startprogram()
