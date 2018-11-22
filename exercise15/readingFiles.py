#Exercise 15
#Reading files
#open() and read() functions


#Run it:
#Terminal, cd to folder, python exercise15.py + filename (real file name)

from sys import argv

script, filename = argv

#Opens the file assigned to the variable named txt
txt = open(filename)

print(f"Here's your file {filename}: ") #{} prints the name of the file
print(txt.read()) #reads (prints the content of) the file

print("Type the filename again: ")
file_again = input("> ") #saves the filename to the variable 'file_again'
txt_again = open(file_again) #assigns the function to the variable
#txt_again

print(txt_again.read()) #prints the content of the file.