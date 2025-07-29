age = 25

match age:
    case 0 | 1 | 2 | 3 | 4:
        category = "Toddler"
    case 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
        category = "Child"
    case 13 | 14 | 15 | 16 | 17 | 18 | 19:
        category = "Teenager"
    case 20 | 21 | 22 | 23 | 24 | 25 | 26:
        category = "Young Adult"
    case _:
        category = "Adult"

print(category) 

#nested conditions scenario
#club Entry --> if age is 21 or above and also a valid id shoud be present 
age = 22
has_id  = True 

if age >= 21:
    if has_id:
        print("you can enter the club")
    else:
        print("you need id to enter the club") 
else:
    print("you are not eligible to enter the club")

