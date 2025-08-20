#lme-->sub feature - student management system 
#system information -->tuples
SYSTEM_INFO = ("LMS Student portal","v.10","2015","Edify university")
ADMIN_INFO = ("admin@edify.ai","9059479273","201")

#display system info 
print("="*50)
print(f"welcome To {SYSTEM_INFO[0]}")
print(f"Developed by {SYSTEM_INFO[3]}")
print("="*50)

#store all students --> dictionary 
students = {}

#start with option selection 
while True:
    print("choose an option from (1-5):")
    print("1 - Add student")
    print("2 - update student")
    print("3 - delect student")
    print("4 - list all  student")
    print("5 - exit student")

    choice = input("Enter your choice:")
    if choice =="1":
        print("performing operation 1")
        student_id = input("Enter student ID:")
        #student exists
        if student_id in students:
            print("students already with this id exixts in system")
        else:
            name = input("Enter student name:").title()
            #store multiple scores 
            scores = []
            while True:
                score_input = input("Enter a score or type done:")
                #validate if input is number or done 
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0<= score <=100:
                        scores.append(score)
                    else:
                        print("score should be between 0-100")
                else:
                    print("score should be number only")
            # After collecting scores, store student info
            students[student_id] = {"name": name, "scores": scores}

        #store multiple unique skills
        skill = set()
        while True:
            skill_input = input("Enter aq skill or type done:")
            if skill_input =="done":
                break
            skill.add(skill_input.strip().title())
        
        #save students details received so far 
        students[student_id] = {
            "name": name,
            "scores": scores,
            "skills": skill
        }
        print("student added successfully!")

        #for verification 
        print(students)


    elif choice =="2":
        print("performing operation 2")
    elif choice =="3":
        print("performing operation 3")
    elif choice =="4":
        print("performing operation 4")
    elif choice =="5":
        print("performing operation 5")
        break
    else:
        print("invalid choice only(1-5) available ")
          


