#implementation of loops

#while loop 
#while condition:
#statements

count = 1
while count <=5 :
    print(count)
    count +=1

#Best usecase to understand while 
password = "python456"
user_input = ""

while user_input != password:
    user_input = input("Enter the password:")
    print("access granted")

#for loop
# for elements in sequence # we can not use for to itearte non iterate objects
# stetements
text = "python"
print(dir(text))
for i in text:
       print(i)

#num = 10 #we can use iterste iteratable objects pyt
just_num = 10
print(dir(just_num))
#for i in num: 
   # print(i)

#manual work
print("hi")

#say 10 times hi (manually)
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")

print("==============")


#say 10 times hi (automated)
for i in range(10):
     print("hi")

     for i in range(3,10):
          print("hello")

#LETS print even  numbers between 1 - 20 --> while 
#1st approach 
i = 2
while i <= 20:
     print(i)
i+=2
print("==============")

#2nd approach 
i = 2
while i <= 20:
     if i % 2 == 0:
          print(i)
          i += 1
     print("==============")

 #nested forloop 
 #mathtable
     for i in range(1,4):
          for j in range(1,11):
               print(f"{i} * {j} = {i*j}")

#break demo
for i in range(5):
     if i == 3:
          break #terminate tha loop when i is 3
     print(i)

 #conyinue demo
for i in range(5):
     if i == 3:
          continue #skip the 4th  iteration when i is 3
     print(i)

     #pass demo
     if(5>9):
          pass #do nothing  