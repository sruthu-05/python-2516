#define a list 
empty_list = []
print(type(empty_list))
print(empty_list)

#define a list with numbers 
list_nums = [10,20,30,40,50]
print(type(list_nums))
print(list_nums)

#define a list with text data 
list_courses = ["python","java","cloud","devops","html"]
print(type(list_courses))
print(list_courses)

#define a list with mixed data 
list_mixed = [10,20,30,"java","cloud","devops","html"]
print(type(list_mixed))
print(list_mixed)

#list inside list
list_nest = [10,20,30,40,50,["java","cloud","devops","html"]]
print(type(list_nest))
print(list_nest)

#using class list
empty_list = list()
print(type(empty_list))
print(empty_list)

#define a list with numbers 
list_nums =list([10,20,30,40,50]) 
print(type(list_nums))
print(list_nums)

#define a list with numbers 
num = 10
print(type(num))
#list_nums =list(10) # type erroe : 'int' object is not defined
list_nums =list([10]) 
print(type(list_nums))
print(list_nums)

#Acessing the data in list
list_nums = [10,20,30,40,50]
first_list_nums = list_nums[0]
last_list_nums = list_nums[-1]

#indexing 
print(first_list_nums)
print(last_list_nums)

#slicing
list_nums = [10,20,30,40,50]
print(list_nums[:])
print(list_nums[1:4:-1])
print(list_nums[1:4:1])
print(list_nums[::-1])

#get to knoe memory management with data 
num1 = 10
num2 = 10

print(id(num1))
print(id(num2))

list_nums_1 = [10,20,30,40,50]
list_nums_2 = [10,20,30,40,50]

print(id(list_nums_1))
print(id(list_nums_2))

print(id(list_nums_1[0]))
print(id(list_nums_2[0]))
print(id(num1))
print(id(num2))

#if we access index out of range , we get index error
list_nums_1 = [10,20,30,40,50]
#print(list_num[10])
#print(dir(list_nums))

#looping can be done as its an iterable 
list_nums_1 = [10,20,30,40,50]
for i in list_nums:
    print(i)

    #using range 
    custom_list = list(range(0,26,5))
    print(custom_list)


#perfome any operations with operations 
custom_list = list(range(0,26,5))
for i in custom_list:
         print(i*2)
    
 #perfome some conditionals 
days = ("sun","mon","tue","wed","thu","fri","sat")
day = input("Enter day name in a week")
if day in days:
       print("day exists")
else:
       print("invalid day")
       
 #duplicates are allowed       
list_nums = [10,20,30,40,50,50,50,30] 
print(list_nums)

#list operations 
list_nums = [10,20,30,40,50]
print(dir(list_nums))

#append() --> adds a single element 
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.append(60)
print(list_nums)

#list_nums.append(70,80)# only takes one argement 
#print(list_nums)

#note noth append and extend takes only one argument 

list_nums.extend("hello")
print(list_nums)

#insert() --> based on index insert an element 
list_nums = [10,30,40,50]
print(list_nums)
list_nums.insert(1,20)
print(list_nums)

#To add end of the list we can use len 
list_nums.insert(len(list_nums),60)
print(list_nums)

list_nums.insert(10,100)
print(list_nums)
#print(list_nums.index(100))

#soft copy - use assignment operators 
list_nums = [10,20,30,40,50]
print(list_nums)

bk_list_nums = list_nums #soft copying 

#pop() --> removes an element , by default removes last element 
list_nums = [10,20,30,40,50]
print(list_nums)
removed_element =list_nums.pop()
print(removed_element)
print(list_nums)

list_nums = [10,20,30,40,50]
print(list_nums)
removed_element =list_nums.pop(1)
print(removed_element)
print(list_nums)

#remove() --> removes matching value , not based on index 
list_nums = [10,20,30,40,50,10]
print(list_nums)
list_nums.remove(10)
print(list_nums)

#clear() --> removes all the elements 
list_nums = [10,20,30,40,50,10]
print(list_nums)
list_nums.clear()
print(list_nums)

#index() --> removes the index position of element  
list_nums = [10,20,30,40,50]
print(list_nums.index(40))

list_nums = [10,20,30,20,40,20,10,20,10,20,10]
print(list_nums.index(20,2))#start
print(list_nums.index(20,4,8))#start

#count()--> it counts and  returns number of times a element is present 
list_nums = [10,20,30,20,40,20,10,20,10,20,10]
print(list_nums.count(10))

#reverse()--> this method reverses the element and updates the original list 
list_nums = [10,20,30,40,50]
print(list_nums)
print(list_nums.reverse())
print(list_nums)

#slicing  method reverses the element and don't updates the original list 
list_nums = [10,20,30,40,50]
print(list_nums)
print(list_nums[::-1])
print(list_nums)

#sort()--> sorts the list default is ascending 
list_nums = [10,30,20,40,50]
print(list_nums)
asc_sort = list_nums.sort() #ascending
print(list_nums)

list_nums = [10,30,20,40,50]
print(list_nums)
print(list_nums.sort(reverse=True)) #descending
print(list_nums)

names = ["sruthi","monya","siri"]
names.sort()
print(names)

mixed_data = ["sruthi","monya","siri"]
#mixed_data.sort() #mixed data cannot be sorted out 
print(mixed_data)