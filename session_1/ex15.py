#imports argv module
from sys import argv

#setting argument variable names
script, filename = argv

#variable txt, it is equal to opening the file of the name provided in terminal
#for var filename
txt = open(filename)

#txt.read() is reading the open file txt, it is then printed
print "here's your file %r:" % filename
print txt.read()

#now take a raw input for a file name and assign to the variable file_again
print "i'll also ask you to type it again:"
file_again = raw_input(">")

#open file of the name equal to variabel file_again and assign to variable txt_again
txt_again = open(file_again)
#reads the opened file and prints its contents
print txt_again.read()
