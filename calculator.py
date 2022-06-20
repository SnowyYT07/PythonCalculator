import math
import random

def calculator():
	version= "1.0"
	print("Welcome To calculator")
	print("This calculator is in work progress, please understand any bug, and report <3")

	def options():
		print("\nOptions:")
		print("Enter 'add' to add two numbers")
		print("Enter 'sub' to subtract two numbers")
		print("Enter 'mult' to multiply two numbers")
		print("Enter 'divide' to devide two numbers")
		print("Enter 'inf' for informations and help")
		print("Enter 'more' for more operations")
		print("Enter 'leave' to quit the program")
	options()

	while True:
		USER_input = input("\nPlease input your option: ")
    
		if USER_input == "options":
			pass

		elif USER_input == "more":
			print("\nList of more operations")
			print("Enter 'power' to raise a number to the power of another")
			print("Enter 'sqrt' to find the square root of a number")
			print("Enter 'percent' to calculate a percentage of a number ")
			print("Enter 'sin' to find sin of a number")
			print("Enter 'cos' to find cos of a number")
			print("Enter 'tan' to find tan of a number")
			print("Enter 'rand' to get a random  number between 0 and 1")
			print("Enter 'randint' to get a random number between two numbers")
			print("Enter 'pi' to return value for pi")
			print("Enter 'e' to return value for e")
			continue

		elif USER_input == "add":
			try:
				num1 = float(input("Enter the first number:"))
				num2 = float(input("Enter the second number:"))
				result = str(num1 + num2)
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "sub":
			try:
				num1 = float(input("Enter the first number:"))
				num2 = float(input("Enter the second number:"))
				result = str(num1 - num2)
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "mult":
			try:
				num1 = float(input("Enter the first number:"))
				num2 = float(input("Enter the second number:"))
				result = str(num1 * num2)
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "divide":
			try:
				num1 = float(input("Enter the first number:"))
				num2 = float(input("Enter the second number:"))
				result = str(num1 / num2)
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")
			except ZeroDivisionError:
				print("Haha bro you rly try divide 0 by 0? rlyy??")

		elif USER_input == "inf":
			print("\nInformation")
			print("Enter 'options' to view options again")
			print("If error occured it means you didn't input the correct data type")
			print("Yes, you are able to use negative and decimal numbers in this calculator :3")
			print("More updates or help coming soon, until i work in this repo")
			print("###" * 6)
			print("Current version:" + version)
			continue

		elif USER_input == "leave":
			print("\nThanks for use this basic calculator!!")
			break

		elif USER_input == "exit":
			print("\nThanks for use this basic calculator!!")
			break

		elif USER_input == "power":
			try:
				num1 = float(input("Enter the first number:"))
				num2 = float(input("Enter the second number:"))
				result = str(num1**num2)
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "sqrt":
			try:
				num1 = float(input("Enter a number:"))
				result = str(math.sqrt(num1))
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "percent":
			try:
				num1 = float(input("Enter a number:"))
				result = str(num1 / 100)
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "sin":
			try:
				num1 = float(input("Enter a number:"))
				result = str(math.sin(num1))
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "cos":
			try:
				num1 = float(input("Enter a number:"))
				result = str(math.cos(num1))
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "tan":
			try:
				num1 = float(input("Enter a number:"))
				result = str(math.tan(num1))
				print("\nThe awnser is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "rand":
			try:
				result = str(random.random())
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "randint":
			try:
				num1 = float(input("Enter the first number:"))
				num2 = float(input("Enter the second number:"))
				result = str(random.randint(num1, num2))
				print("\nThe answer is " + result)
			except (ValueError, TypeError):
				print("ERROR!")

		elif USER_input == "pi":
			result = str(math.pi)
			print("\nThe answer is " + result)

		elif USER_input == "e":
			result = str(math.e)
			print("\nThe answer is " + result)

		else:
			print("Unknown input")

		options()

calculator()
