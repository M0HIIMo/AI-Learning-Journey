print("---- My First Project ----")

students = []

while True:
    print("\n--- Student Manager ---")
    print("1. Add student")
    print("2. Show all")
    print("3. Average")
    print("4. Top student")
    print("5. Search")
    print("6. Exit")
    
    choice = input("Choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        score = int(input("Enter your score: "))
        information = {"name": name, "score": score}
        students.append(information)
    
        print("Student added!")
    elif choice == "2":
        for student in students:
            print(f"{student['name']}: {student['score']}")
    elif choice == "3":
        if len(students) == 0:
            print("No students yet!")
        else:   
            total = 0
            for student in students:
                total = total + student['score']
            average = total / len(students)
            print(f"Average: {average}") 
    elif choice == "4":
        if len(students) == 0:
            print("No students yet!")
        else:
            top_student = students[0]
            for student in students:
                if student['score'] > top_student['score']:
                    top_student = student
            print(f"Top student: {top_student['name']},with score {top_student['score']}")
    elif choice == "5":
        name = input("Enter name to search: ")
        found = False
        for student in students:
            if student['name'] == name:
                found = True
                print(f"Found: {student['name']}, score: {student['score']}")
        if found == False:
            print("Not founded!")            
    elif choice == "6":
        print("GoodBye.")   
        break       
