def main():
    #NOTE: index 0 is student ID, index 1 is last name, index 2 is first name, index 3 is major, index 4 is GPA
    #read text file list
    studentList = open('students.txt', 'r') #r for read
    students = studentList.readlines() #reads all lines in the file

    #Dictionary to store student data with student ID as key for each line
    studentData = {}
    for line in students:
        data = line.strip().split(',')  # Split each line by comma
        studentData[data[0]] = {
            'Last Name': data[1],
            'First Name': data[2],
            'Major': data[3],
            'GPA': data[4]
        }
    #Print one line of student data
    #print(studentData['001023456'])  # Example to print student Alice Smith
    
    #run program until user chooses to quit
    while True:
        print("Welcome to the Student Database, to search for a student please choose one of the following options:")
        print("1. Search by Last Name")
        print("2. Search by Major")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            lastName = input("Enter the last name of the student: ").strip()
            found = False
            for studentID, data in studentData.items():
                if data['Last Name'].lower() == lastName.lower():
                    print(f"Student ID: {studentID}, Last Name: {data['Last Name']}, First Name: {data['First Name']}, Major: {data['Major']}, GPA: {data['GPA']}")
                    found = True
            if not found:
                print("No student found with that last name.")

        elif choice == '2':
            major = input("Enter the major of the student: ").strip()
            found = False
            for studentID, data in studentData.items():
                if data['Major'].lower() == major.lower():
                    print(f"Student ID: {studentID}, Last Name: {data['Last Name']}, First Name: {data['First Name']}, Major: {data['Major']}, GPA: {data['GPA']}")
                    found = True
            if not found:
                print("No student found with that major.")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
main()

#NOTE: Didn't quite understand what the dictionary had to do with the search given the search had no ID option. If something is missing let me know
