#arthimatic operations 
num1 = 5
num2 = 8
print(num1+num2)
print(num1-num2)
print(num1/num2) #0.625
print(num1*num2)
print(num1%num2)
print(num1//num2) # floor division
print(num1**num2) #exponentiation
 
 #compound assignment operations
num = 15
#num = num + 6
num+=6 
print(num)
num*=8
print(num) 

#comparison / relational operators 
num1 = 5
num2 = 8
print(num1<num2)
print(num>num2) 
print(num!=num2) 
print(num>=num2) 
print(num<=num2) 
print(num==num2) 

#logical operators 
a = 10
b = 5
c = 3
d = 8
result_and = a > b and b < c #T and F -->f
print(result_and)
result_or = a > b and b < c # t and f -> t 
print(result_or)
result_not = a > b and b < c
print(result_not) 

#membership operators
text = "python is eazy"
is_z_present = "z" in text
print(is_z_present)

list_nums={1,5,8,9}
is_5_present = 5 in list_nums
print(is_5_present)

#identity operators 
num1 = 10
num2 = 10
print(id(num1))
print(id(num2))
print(num1 is num2)

num1_list = {10,20}
num2_list = {10,20}
print(id(num1_list))
print(id(num2_list))
print(num1_list is num2_list)
 
print(num1_list is not num2_list)

#bitwise operators
a = 5 #0000000000000101
b = 3 #0000000000000011
resultand = a & b #000000000000001
print(resultand)

resultor = a | b #0000000000000111
print(resultor)

resultxor = a ^ b #0000000000000110
print(resultxor)

resultnot = ~b #
print(resultnot)

#left shift 
b = 3 #011
print(3<<2) #0000000000001100 --> 12 
print(3<<1) #0000000000000110 --> 6
print(3<<3) #0000000001100000 --> 24

#right shift 
b = 3 #0000000000000011
print(3>>2) #00000000000000 --> 0 
print(3>>1) #00000000000001 --> 1
print(8>>3) #0000000000001000 --> 1 

# c = -4 #1111111111111100
print(-4>>3) #1111111111111111 

