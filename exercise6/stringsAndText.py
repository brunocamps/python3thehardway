types_of_people = 10
#using the formatting f from exercise 5 in a variable containing a string
x = f"There are {types_of_people} types of people."

#assigning strings to variables
binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

#formatting and printing {y} inside a string (and y is also a string)
print(f"I also said: '{y}'") #This is important, pay attention here

hilarious = False #boolean type False assigned to variable hilarious
joke_evaluation = "Isn't that joke so funny?! {}" #leave the {} field to be formatted later

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) #sum of strings.

