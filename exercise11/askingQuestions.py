#Get data into our programs
#take some kind of input from a person
#change it
#print out something to show how it changed

#input() saves a string as default
#you can force an int, double...
#int(input())



print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy")

#end=' ' -> this tells print to not end the line with a newline
#character and go to the next line.
