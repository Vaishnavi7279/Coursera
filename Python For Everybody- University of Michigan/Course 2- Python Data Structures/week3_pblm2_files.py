#COURSERA COURSE
#PYTHON FOR EVERYBODY- UNIVERSITY OF MICHIGAN
#SECOND COURSE- PYTHON DATA STRUCTURES

#WEEK 3- WORKING ON FILES
#PROBLEM 2
#Write a program that prompts for a file name
#then opens that file and reads through the file
#looking for lines of the form:X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines 
#compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
#when you are testing below enter mbox-short.txt as the file name.

count=0
total=0
fname=input("Enter file name: ")
fh=open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        num=float(line[21:])
        total=num+total
avg=total/count
print("Average spam confidence:", avg)