#COURSERA COURSE
#PYTHON FOR EVERYBODY- UNIVERSITY OF MICHIGAN
#SECOND COURSE- PYTHON DATA STRUCTURES

#WEEK 3- WORKING ON FILES
#PROBLEM 1
#Write a program that prompts for a file name, then opens that file and reads through the file
#Print the contents of the file in upper case
#Use the file words.txt to produce the output below

input("Enter File Name")

fhand = open ("words.txt")
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)