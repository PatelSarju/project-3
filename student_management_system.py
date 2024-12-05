print("Welcome to the student management system!")

student_list=[]
id_set=set({})

is_on=True

while is_on:
    choice=int(input("\nSelect an option:\n1. Add student\n2. Display all students\n3. Update student information\n4. Delete student\n5. Display Subjects Offered\n6. Exit\nEnter your choice:"))

    if choice==1:
        print("\nEnter student details:")
        student_id=int(input("Student ID:"))
        while student_id in id_set:
            print("\nThis id already exist in the system!")
            print("Please enter the new employee id!")
            student_id=int(input("Student ID:"))
        else:
            id_set.add(student_id)
        name=input("Name:").title()
        age=int(input("Age:"))
        grade=input("Grade:").title()
        dob=input("Date Of Birth (DD-MM-YYYY):")
        subjects=input("Subjects (comma-seprated):").title()
        student_list.append({'Student_id':student_id,'Name':name,'Age':age,'Grade':grade,'Subjects':set(subjects.split(',')),'Date_of_birth':dob})
        print("\nStudent added successfully!")
        
    elif choice==2:
        if student_list:
            print("\n--- Display All Students ---\n")
            for i in student_list:
                for j,k in i.items():
                    print(f"{j}:{k}")
                print() 
        else:
            print("No such students records found!")
        
    elif choice==3:
        id=int(input("\nEnter the student id which student's data you want to update:"))
        if id in id_set:
            for i in student_list:
                if id==i['Student_id']:
                    detail=input("\nWhich detail you want to update:").title()
                    if detail=='Student_id':
                        print("You can't update student ID.")
                    elif detail=='Name':
                        new_name=input("\nEnter the new name:").title()
                        i[detail]=new_name
                        print("\nName updated successfully!")
                    elif detail=='Age':
                        new_age=int(input("\nEnter the new age:"))
                        i[detail]=new_age
                        print("\nAge updated successfully!")
                    elif detail=='Grade':
                        new_grade=input("\nEnter the new grade:").title()
                        i[detail]=new_grade
                        print("\nGrade updated successfully!")
                    elif detail=='Subjects':
                        new_subjects=input("\nEnter the new subjects (comma-seprated):").title()
                        i[detail]=set(new_subjects.split(','))
                        print("\nSubjects updated successfully!")
                    elif detail=='Date_of_birth':
                        print("\nYou can't change your date of birth!")
                    else:
                        print("\nYou entered the wrong key name!")
                        break
        else:
            print("\nYour entered id is not found in the system!")
            
    elif choice==4:
        id=int(input("\nEnter the id which student's data you want to remove:"))
        if id in id_set:
            for i in student_list:
                if id==i['Student_id']:
                    del student_list[student_list.index(i)]
                    id_set.remove(id)
            print("\nStudent data has been removed successfully!")
        else:
            print("\nEntered id is not found in the system!")
    
    elif choice==5:
        id=int(input("\nEnter the student id which student's subject you want to see:"))
        for i in student_list:
            if id==i['Student_id']:
                print(f"\nWe offer the subjects are {[i for i in i['Subjects']]}")

    elif choice==6:
        print("\nYou are exit from the system!")
        is_on=False
    
    else:
        print("You entered the wrong choice!")
        is_on=False