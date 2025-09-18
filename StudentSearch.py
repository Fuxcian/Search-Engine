def main():
    #NOTE: index 0 is student ID, index 1 is last name, index 2 is first name, index 3 is major, index 4 is GPA
    
    try: 
        studentList = open('students.txt', 'r') # read more
        students = studentList.readlines() # reads all lines into a list

        # creates a list
        studentData = {}
        # inserts terms into dictionary
        for line in students:
            # each line is a list of student information
            data = line.strip().split(',')  # takes each list and splits it into parts and removes whitespace
            studentData[data[0]] = { # student ID is the key
                # other values in list are assigned to terms and keys; key-value pairs
                'Last Name': data[1],
                'First Name': data[2],
                'Major': data[3],
                'GPA': data[4]
            }
        while True: # keeps loop going until quit
            print("Welcome to the Student Database, to search for a student please choose one of the following options:")
            print("1. Search by Last Name")
            print("2. Search by Major")
            print("3. Quit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                lastName = input("Enter the last name of the student: ").strip() # strip removes whitespace
                found = False # boolean to check if any student is found
                for studentID, data in studentData.items(): # studentID is key, data is value in dictionary; items() returns key-value pairs
                    if data['Last Name'].lower() == lastName.lower(): # compares inout to key value; lower() makes it case insensitive
                        print(f"Student ID: {studentID}, Last Name: {data['Last Name']}, First Name: {data['First Name']}, Major: {data['Major']}, GPA: {data['GPA']}")
                        found = True # boolean is true, therefore if condition is met
                if not found: # boolean is false, therefore if condition is not met
                    print("No student found with that last name.")

            # repeat above for major
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

    except FileNotFoundError:
        print("Error: The file 'students.txt' was not found.")
        return
    
main()
