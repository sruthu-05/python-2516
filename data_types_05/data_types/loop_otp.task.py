#otp  / verification code simulation
import random 

otp = random.randint(1000, 9999)# generate a random 4 didgit number 
print(otp)

#logic 
attempts = 3

while attempts:
    user_otp = int(input("Enter the otp:"))
    if len(str(user_otp))!= 4:
        print("Please enter a 4-digit number")
        if user_otp == otp:
            print("access granted")
            break 
        attempts-=1
    else:
         print("invalid otp please try again")
        