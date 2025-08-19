#empty set
empty_set = {} #this is  dict
print(type(empty_set))
print(empty_set)

#use set class 
empty_set = set() #this is set 
print(type(empty_set))
print(empty_set)

#print(dir(empty_set))

#numbers set 
set_nums = {10,20,30,40,50}
print(set_nums) #{50,40,30,20,10}-->unordered

#deplicates eleminated
set_nums = {10,20,30,40,50,10,20} # deuplicates are 10,20
print(set_nums) # only unique elements 

#index will not work
set_nums = {10,20,30,40,50}
#rint(set_nums[2]) #typeErroe: 'set' object is not subscriptable --> we cannot use index -->unindex 

#text dict
set_text = {"python","java","js"}
print(set_text)

#mixed dict
set_mixed = {"python","java","js",10,20,30,40,50,4.5}
print(set_mixed)

#Accessing data in sets 
set_nums = {10,20,30,40,50}
#print(set_nums[2])no indexing with sets 
#print(dir(set_nums)) --> set is iterable 
for i in set_nums:
    print(i)

    list_nums = list(set_nums)
    print(list_nums)
    print(list_nums[1])

 #operations / methods on sets 

#add() --> add an element to set 
s1 = {10,20,30,40,50}
s1.add(50)
s1.add(60)
print(s1)
#S1.add((70,80))
s1.add((70,80))
print(s1)

#update()--> adds multiple elements from iterables only
s1 = {10,20,30,40,50}
#s1.update(60)
print(s1),
s1.update((80,90,100),[10,20,40]) # accepts multiple arguments
print(s1)

#remove()--> removes  a specific element, raises error if not found 
s1 = {10,20,30,40,50}
#s1.remove(60) keyError: 60
s1.remove(10)
print(s1)

#discard()--> removes  a specific element , raises no error if not found 
s1 = {10,20,30,40,50}
s1.discard(60)
print(s1)
s1.discard(10)
print(s1)

#clear() --> removes all eements 
s1 = {10,20,30,40,50}
s1.clear()
print(s1)

#pop()-->removes  an random/arbitray elements
s1 = {10,20,30,40,50}
s1.pop()
print(s1)

#set specific operations 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

#union()--> combines elements from both sets 
print(s1.union(s2))
print(s1 | s2)

#intersection() --> extract only common elements
print(s1.intersection(s2))
print(s1 & s2)

#intersection_update()--> extracts only commom elements , update the calling  set 
print(s1)
print(s1.intersection_update(s2))
print(s1)
print(s2)

#difference()--> removes the element which also occur in other set 
print(s1)
print(s1.difference(s2))
print(s1-s2)

#difference_update ()--> removes the element which also occur in other set , and update the calling set 
print(s1)
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

#symmetric_difference ()--> removes common elements and take combine elements left in both set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s2^s1)
print(s1)
print(s2)

#issubsewt()--> check if the given set subset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50} #true
#s2 = {60,40,50} false 
print(s2.issubset(s1))

#issuperset()--> check if the given set superset of aother set
s1 = {10,20,30,40,50}
s2 = {40,50} #true 
print(s1.issubset(s2))
print(s2.issubset(s1))

#isdisjointset()--> chekc if 2 sets have no common elements 
s1 = {10,20,30,40,50}
#s2 = {40,50} #false
s2 = {60,70,80} #true 
print(s1.isdisjoint(s2))


#copy()-->created a shallow copy
s1 = {10,20,30,40,50}
s2 = s1.copy()
print(s1)
print(s2)

s2.add(80)
print(s1)
print(s2)

#print(dir(s1))
s1 = {10,20,30,40,50}#regular set
#fs = {10,20,30,40,50} this is also a set 

#frozen can be created by using class
fs = frozenset({10,20,30,40,50})
print(type(fs))
print(fs)
#print(fs.add(60)) #AttributeError: 'frozenset' object has no attribute 'add'
print(dir(fs))

#frozenset operations 
fs1 = {10,20,30,40,50}
fs2 = {40,50,60,70,80}

print(fs1.union(fs2))

 

 
