

while True:
    input1 = input("1. Enter a Student\n2. Quit\n")
    if input1 == "1":
        lName = input("Enter the students last name: ")
        if lName == "ZZZ":
            quit()
        fName = input("Enter the students first name: ")
        studentGPA = float(input("Enter the students GPA: "))
        if studentGPA >= 3.5:
            print("This student has made the Deans List.")
        if studentGPA >= 3.25:
            print("This student has made Honor Roll.")
    elif input1 == "2":
        quit()
    elif input1 != "1" and input1 != "2":
        print("Please choose an option.")

    


