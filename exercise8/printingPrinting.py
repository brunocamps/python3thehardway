formatter = " {} {} {} {} "
formatter2 = " {} " #only {} can receive values/format in python
formatter3 = " () "

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

#print(formatter.format("one")) -> will return an error
#If you print formatter, it will print just as you've declared
#formatting the variable will change it's values
#to the values you want to format it to


print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song"
))

print(formatter2.format("one"))
print(formatter3.format("one2")) #formatting doesn't work here

#In python, {} for formatting...