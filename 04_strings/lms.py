#Enhance lms grade tracker with string operations 

print("=" * 30)
print("Enhance lms grade trackrer")
print("=" * 30)

#validate the id
student_id_valid = False 
while not student_id_valid:
    student_id = input("Enter your id: ")
    #condition : check if valid id based on negative sign
    if student_id.startswith("-") and student_id[1:].isdigit():
         print("Please enter positive  value only")
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0: 
            student_id_valid = True
        else:
            print("Please enter non-zero value")
    else:
        print("Enter only numbers") 

print(student_id)
 #format id 
formatted_id = "STU" + str(student_id).zfill(5)
print(formatted_id)


#validate name 
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter your name")
    #student_name = student_name.strip().capitalize()
    student_name = student_name.strip().title()
    #strip will only remove front and back spaces not in between 

    #name check should have only alphabets 
    name_check = student_name.replace(" ","")

    #look only for alphabets
    if name_check.isalpha() and len(student_name) >= 3:
        student_name_valid = True
        print("Name: " + student_name)
    else:
        if not name_check.isalpha():
            print("Name should contain only letters")
        elif len(student_name) < 3:
            print("Name should have at least 3 letters")

#email generation 
name_part = student_name.split()
#print(name_part)
first_name = name_part[0].lower()
#print(first_name)

student_email = first_name+"."+str(student_id) + "@university.edu"
print(student_email)

#discount calculator 
base_course_fee_valid = False 
while not base_course_fee_valid:
    base_course_fee = input("Enter your course fee: ")
    #condition : check if valid id based on negative sign
    if base_course_fee.startswith("-") and base_course_fee[1:].isdigit():
        print("Please enter positive  value only")
    elif base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 0: 
            base_course_fee_valid = True
        else:
            print("Please enter non-zero value")
    else:
        print("Enter only numbers") 
    
    #calculator 
    discount = 0
    print("Enter  description")
    description = input()

if description.lower().find("Reference") != -1:
     discount+=5000

if "scholarship" in description:
     discount+=7000
     
if "promo" in description:
    discount+=3000   

final_fee = base_course_fee - discount

print(f"Base course fee: {base_course_fee}")
print(f"You got discount: {discount}")
print(f"After discount pay: {final_fee}")

