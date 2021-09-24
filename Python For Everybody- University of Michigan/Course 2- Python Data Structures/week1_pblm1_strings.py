#COURSERA COURSE
#PYTHON FOR EVERYBODY- UNIVERSITY OF MICHIGAN
#SECOND COURSE- PYTHON DATA STRUCTURES

#WEEK 1- STRINGS SLICING FIND
#PROBLEM 1
#Write code using find() and string slicing to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('0')
num=float(text[pos:pos+6])
print(num)