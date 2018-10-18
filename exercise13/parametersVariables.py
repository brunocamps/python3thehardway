#Parameters, Unpacking, Variables
#Write a script that accepts arguments.

from sys import argv
#read the WYSS section for how to run this

#WTF is argv?
#https://www.quora.com/What-is-sys-argv-in-python-and-how-is-it-used

script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

fourth = input("Fourth variable? ")
print(f"Your fourth variable is: {fourth}")


#To run, you have to pass in the values
#Use terminal
# python [file path]parametersVariables.py first 2nd 3rd
