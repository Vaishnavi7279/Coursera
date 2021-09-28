#COURSERA COURSE
#PYTHON FOR EVERYBODY- UNIVERSITY OF MICHIGAN
#SECOND COURSE- PYTHON DATA STRUCTURES

#WEEK 4- PYTHON DATA STRUCTURES: LISTS
#PROBLEM 1
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.

file=input("Enter file name: ")
data=open(file)
lst=list()                       
for line in data:                   
    text=line.rstrip()
    word=text.split()    
    for i in word:               
        if(i in lst):         
            continue               
        else:                     
            lst.append(i)         
lst.sort()                         
print(lst)