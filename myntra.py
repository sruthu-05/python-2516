student_name  =  input("enter student name: ")
grade_level = int(input("enter student grade level: "))
base_fee = float(input("Enter base tuition fee: "))
discount_percentage  = 0
is_topper = input("is the student an academic topper? (yes/no): ")
#input validation
if grade_level < 1 or grade_level > 12:
    print("error: grade level must be between 1 and 12.")
else:
    #determine base discount percentage 
    if grade_level >= 9 and grade_level <= 12:
        if is_topper == "yes":
            discount_percentage = 20
        else:
            discount_percentage = 10
    elif grade_level >= 6 and grade_level <= 8:
        discount_percentage = 5
    else:
        discount_percentage = 0
    
    #match case
    match grade_level:
        case 10:
            discount_percentage += 3
        case 12:
            discount_percentage += 5
        case _:
            pass

    #discount calculation 
    discount_amount = (discount_percentage / 100) * base_fee
    final_fee = base_fee - discount_amount

    #output summary 
    print(f"student name        : {student_name}")
    print(f"grade level         : {grade_level}")
    print(f"academic topper     : {'yes' if is_topper == 'yes' else 'no'}")
    print(f"base tuition fee    :  ₹{base_fee:.2f}")
    print(f"Total Discount      : {discount_percentage:.2f}%")
    print(f"Discount Amount     : ₹{discount_amount:.2f}")
    print(f"Final Tuition Fee   : ₹{final_fee:.2f}")