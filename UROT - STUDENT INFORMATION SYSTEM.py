#############  UROT, JHERYLL E. #################
#############  BS - STATISTICS II ###############
####### SIMPLE STUDENT INFORMATION SYSTEM #######

import csv

Student_Attr = ['Name', 'ID Number', 'Year Level', 'Course', 'Gender']
Student_database = 'Studentsdata.csv'

def main():
    print("-------------------------------------")
    print("      Student Information System     ")
    print("-------------------------------------")
    print("1. Add New Student")
    print("2. Display List of Students")
    print("3. Search Student")
    print("4. Edit Student")
    print("5. Delete Student")
    print("6. Quit")


# Add student
def add_stud():
    print("---------------------")
    print("     Add Student     ")
    print("---------------------")
    
    global Student_Attr
    global Student_database
    
    student_data = []
    for field in Student_Attr:
        value = input("Enter " + field + ": ")
        student_data.append(value)
        
    with open(Student_database, "a", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
    
    print("Data saved!")
    input("Press any key to continue.")
    return

# Display list of students
def display_students():
    global Student_Attr
    global Student_database
    
    print("------------------------")
    print("    List of Students    ")
    print("------------------------")
    
    with open(Student_database, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for x in Student_Attr:
            print( x, end = "\n   ")
        print("\n----------------------------------------------------------")
        
        for row in reader:
            for item in row:
                print( item, end = "\n   ")
            print("\n")
            
    input("Press any key to continue.")

    
# Search student based on ID number
def search_stud():
    global Student_Attr
    global Student_database
    
    print("------------------------")
    print("     Search Student     ")
    print("------------------------")
    
    id_number = input("Enter student's ID Number to search: ")
    with open(Student_database, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if id_number == row[1]:
                    print("Student with ID number ", id_number, "found!")
                    print("Name: ", row[0])
                    print("ID Number: ", row[1])
                    print("Year Level: ", row[2])
                    print("Course: ", row[3])
                    print("Gender: ", row[4])
                    break
        
        else:
            print("Student does not exist.")
    input("Press any key to continue.")


# Update record of a student
def update_record():
    global Student_Attr
    global Student_database
    
    print("----------------------------------")
    print("     Update Record of Student     ")
    print("----------------------------------")
    
    id_number = input("Enter ID Number to update student's record: ")
    index_student = None
    updated_data = []
    with open(Student_database, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_number == row[1]:
                    index_student = counter
                    print("Student Found: at index ", index_student)
                    student_data = []
                    for field in Student_Attr:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1
                
    # Check if the record is or not found
    if index_student is not None:
        with open(Student_database, "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    
    else:
        print(" Student's ID Number not found")
        
    input("Press any key to continue")
    
    
# Delete or remove student from the list
def remove_student():
    global Student_Attr
    global Student_database
    
    print("------------------------")
    print("     Remove student     ")
    print("------------------------")
    
    id_number = input("Enter ID Number of student you want to remove: ")
    student_Found = False
    updated_data = []
    with open(Student_database, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_number != row[1]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_Found = True
    
    if student_Found is True:
        with open(Student_database, "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student with ID Number ", id_number, "has been removed.")
    
    else:
        print("ID Number not be found.")
    
    input("Press any key to continue.")


#main
while True:
    main()
    
    choice = input("Select number 1-6 do you want to do in SIS: ")
    if choice == '1':
        add_stud()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_stud()
    elif choice == '4':
        update_record()
    elif choice == '5':
        remove_student()
    else:
        break



print("------------------------------------")
print("     SYSTEM DISMISSED!              ")
print("------------------------------------")