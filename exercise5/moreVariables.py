#Every time you put text inside "", you're  coding a string
#You print strings, save strings to files, send strings to web servers...
#In this exercise: how to make strings that have variables embedded in them.


#You embed variables inside a string by using a special {} sequence and then
#put the variable you want inside the {} characters.

#You must also start the string with the letter f for "format".
#This little f before the double-quote and the {} tell python 3 that the string need to
#be formatted

my_name = 'Bruno Camps'
my_age = 22
my_height = 1.83 #meters
my_weight = 65 #kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}")
print(f"He's {my_height} meter tall.")
print(f"He's {my_weight} kilos heavy.")
print(f"Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")

print(f"Height {my_height} meters, in inches = {my_height * 39.37} inches")
print(f"Weight {my_weight} kilos in pounds = {my_weight * 2.20} pounds")

print("\nHere's an example of a non formatted string with a variable inside {}: ")
print("His teeth are usually {my_teeth} depending on the coffee.")

#Round a floating point formatted inside a string. Use of round() function.
print(f"Rounded weight in pounds: approx. {round(my_weight * 2.20)} pounds.")
