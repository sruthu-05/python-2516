#using "" or '' of """ is valid for string line strings 
data_1 = "Hello"
data_2= 'hello'
data_3 = """hello"""
data_4 = '''hello'''

print(data_1)
print(data_2)
print(data_3)
print(data_4)

#multiple line string """ are mandatory
# below line is invalid  
#python_string  = ""Python is a high-level, interpreted, general-purpose programming language""

python_string  ="""Python is a high-level, interpreted, general-purpose programming language"""

question = "howa are you ?"
#using  a single quote inside single quotes is not valid 
#if u want to include single quote , use double quotes

#answer = 'i' an fine'
answer = "i'm fine"
print(answer)

#answer = "im "good""
#using double quotes inside double quotes is not valid 
# if u want to include duble quote use singke quote  
answer = 'im"good"'
print(answer)

# is u need to include both singe quote and doublew quote in a astring 
#if u need both use ''' or """
answer = """ i'm fine and "good" """
print(answer)

#Accessing strting characters
text = "python"

#python uses indexing to accessing individual characters in a sting 
#positive indexing starts from 
#always[]
print(text[0])
print(text[2])

print(text[-2])

#invalid range
#print(text[10]) #indexerror : String index out of range 

text = "python"
#using for loop for assess each charater in a astring \
for i in text:
    print(i)

 #using range to acess each character ina astring 
text = "python"
print(text[1])
print(text[2])
print(text[3])

text = "python is very easy yo learn"

#slicing
text = "python"
print(text[0:3]) #last index is excluded -->pyt
print(text[1:4]) #last index is excluded -->yth
print(text[1:]) #last index is excluded -->ython
print(text[:4]) #last index is excluded -->pyton
print(text[2:5]) #last index is excluded -->tho
print(text[2:]) #last index is excluded -->thon
print(text[:]) #last index is excluded -->python

#is step is not defined it ios 1 by default
print(text[0:6:2]) #last index is excluded -->pto
print(text[1:4:1]) #last index is excluded -->yth
print(text[0:4:2]) #last index is excluded -->pt

text = "pythonisveryeasyyolearn"
print(text[0:16:2]) #last index is excluded -->ptoivres

#for negative indexing  default step is 1
#text = "python" #valueError: slice step cannot be zero 
print(text[1:4:])

text = "python"
print(text[-4:-1]) # tho 
print(text[-6:-3]) # pyt
print(text[-4:-1:-1])
#  0  1  2  3  4  5 (positive index)
#  p  y  t  h  o  n 
# -6 -5 -4 -3 -2  -1 (negative index)
text = "python"
#start = -4 -->index -->3 -->t
#end = -1 -->index -->5 -->n (excliuded)
#step = -1 --> move backwards

#NOTE: u are starting at index 2 and trying to go backward to index 5 --> nothing will be printed 
text = "python"
print(text[1:4:-1])  
#  0  1  2  3  4  5 (positive index)
#  p  y  t  h  o  n 
# -6 -5 -4 -3 -2  -1 (negative index)
#start = 1 -->index -->1 -->y
#end = 4 -->index -->4 --> o (excliuded)
#step = -1 --> move backwards 

#typical use case of slicing of backward step 
text = "python"
print(text[::-1]) 

#string immutability 
text = "python"
#text[0] = "P" #TypeError: 'str' object does not support item assignment
print(text)

#reassigning is valid 
text = "python"
text = "Python" #new
print(text)

new_text = "j" + text[1:]#new
print(new_text) #jython

#cancat and repeatation 
#cancatination --> join multiple strings together 
text1 = "python"
print(text[4:0:-1]) #ohty
print(text[-2:-6:-1]) #ohty 

#repetation --> repeat a string multiple times 
str = "hi"
print(str * 5) #hihihihihi

#string operations -->  string methods 
print(dir(str))

mobile_number = input("Enter mobile number")
valid_number = mobile_number.isdigit()
print(valid_number)

 
pan_number = input("Enter pan card number ")
valid_number = pan_number.isalnum()
format_valid_pan_number = pan_number.upper()

#Every method functionality 
print(help(str.isupper))

#slicing backwards 
print(text[1:4:-1]) #empty
print(text[-1:-4:-1]) #noh
print(text[-4:-6:-1]) #ty
print(text[4:1:-1]) #oht
print(text[5:2]) #empty
print(text[5:2:-1]) #noh
print(text[10:]) # indexingerror = string index out of range 

 