#dictionaries
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

#list --> [10,20,30]
#tuples --> (10,20,30)
#dictionaries --> {key:value}

#numbers dict 
dict_nums ={1:10,2:20,3:30}
print(dict_nums)
print(dict_nums[3])

#text dict
dict_text ={"course1":"python","course":"cloud","course3":"java"}
print(dict_text)
print(dict_text["course1"])

#mixed data 
dict_mixed ={1:10,"course1":"python"}
print(dict_mixed)
print(dict_mixed["course1"])

#dict inside dict 
students ={
    "101":{
        "name": "sruthi",
        "email": "sruthi4689@gmail.com",
        "course": "python"
    },
    "102": {
        "name": "mini",
        "email": "mini8109@gmail.com",
        "course": "java"
    },
    "103":{
        "name": "siri",
        "email": "siri123@gmail.com",
        "course": "devops"
    }
}
print(students)
        
#incorrect
#nums = {[1,2,3];"python"} # type Error : unhasable type error 
#print(nums)

nums = {(1,2,3):"python"}
print(nums)

#This is possible 
dict_sub_dict = {101: ["sruthi", "java", "9am"], 102: ("sruthi", "python", "8am")}
print(dict_sub_dict)

#update data --> menthods 
fruits = {"a":"apple","b":"banana"}
print(fruits)
#use assignment  to add new item
fruits["c"] = "cherry"
print(fruits)

#use assignment to update existing item 
fruits["a"] = "apricot"
print(fruits)

#class dict same as lists and tuples
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

#list --> [10,20,30]
#tuples --> (10,20,30)
#dictionaries --> {key:value}

#numbers dict
dict_nums = dict({1:10, 2:20, 3:30})
print(dict_nums)
print(dict_nums[3])

#dict operations 
print(dir(dict_nums))

#update()--> adds or updates dict items 
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.update({"c":"cherry"})
print(fruits)

#pop()-->removes items with specified keys 
fruits = {"a":"apple","b":"banana"}
print(fruits)
#uits.pop("c") # keyEror: "c"
fruits.pop("b")
print(fruits)

#fruits.pop() #keyError:atleast 1arguments , got 0
print(fruits)

#clear() --> removes all items 
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.clear()
print(fruits)

#access related methods 

#get() --> get the value for key 
dict_nums = dict({1:10, 2:20, 3:30})
print(dict_nums)
print(dict_nums[3])

print(dict_nums.get(0)) # if key is not present no error 

#keys() --> returns all the keys only 
dict_nums = {1:10, 2:20,3:30}
print(dict_nums)

dict_nums = {1:10, 2:20,3:30}
only_keys = dict_nums.keys()
for i in only_keys:
    print(i)

#values()-->returns all the values
dict_nums = {1:10, 2:20,3:30}
print(dict_nums.values())

dict_nums = {1:10, 2:20,3:30}
only_values = dict_nums.values()
for i in only_values:
    print(i)

#items() --> returns both keys and values 
dict_nums = {1:10, 2:20,3:30}
print(dict_nums.items())

#copy()--> creates a shallow copy 
dict_nums = {1:10, 2:20,3:30}
bk_dict_nums = dict_nums.copy()

print(dict_nums)
print(bk_dict_nums)

bk_dict_nums.update({4:400})

print(dict_nums)
print(bk_dict_nums)

#soft copy using assignment 
dict_nums = {1:10, 2:20,3:30}
_dict_nums = dict_nums

print(dict_nums)
print(bk_dict_nums)

bk_dict_nums.update({4:400})

print(dict_nums)
print(bk_dict_nums)

#set default()--> returns value of a key , of not present sets it 9
#if the key is present , will not update 
dict_nums = {1:10, 2:20,3:30}
print(dict_nums)

dict_nums.setdefault({3:400})
print(dict_nums)

dict_nums = {1:10, 2:20,3:30,1:100}
print(dict_nums)

#sets concept 