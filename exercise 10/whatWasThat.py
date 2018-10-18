#Wrap pup
#\n (backslash n) puts a new line character into the string at that point
#\ encodes difficult-to-type characters into a string.
#Escape sequences available for different characters
#Escape sequence: tell python what you really want to express

#Page 61: all escape sequences that python supports.


# \t: means a tab
# \n: means splitting to the next line.

tabby_cat = "\tI'm tabbed in."

persian_cat = "I'm split\non a line."

backslash_cat = "I'm \\ a \\ cat." #prints single \

fat_cat = """

I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
