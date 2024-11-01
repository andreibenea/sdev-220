# Author: Andrei Benea
# File Name: student_qualifications.py
# Description: This app accepts student names and GPAs, checks if they qualify for the Dean's List or Honor Roll,
#              and displays a message for each student based on their GPA. The app will stop processing when the
#              last name 'ZZZ' is entered.

while True:
    last_name = input(
        "Type in a student's last name to begin processing or ZZZ to quit: "
    )
    if last_name.isalpha() == True:
        while last_name != "ZZZ":
            first_name = input("Type in student's first name: ")
            while True:
                try:
                    gpa = float(input("Type in student's GPA: "))
                    if gpa < 0 or gpa > 4:
                        print("Invalid GPA input. Please try again!")
                        continue
                    break
                except ValueError:
                    print("Invalid GPA input. Please try again!")

            if gpa >= 3.5:
                print(
                    f"{first_name.capitalize()} {last_name.capitalize()} has made the Dean's List!"
                )

            elif gpa >= 3.25:
                print(
                    f"{first_name.capitalize()} {last_name.capitalize()} has made the Honor Roll!"
                )

            else:
                print("GPA too low for either Dean's List or Honor Roll.")

            print("Student processing complete.")

            last_name = input(
                "Type in a student's last name to begin processing or ZZZ to quit: "
            )
        break
    else:
        print("Invalid student name input. Please try again!")
