# Asks the user to input the number of students in a class.
numStud = int(input("Enter number of student\n"))

# Create empty list to hold data
gradeList = []
allScores = []
try:
    for stud in range(numStud):
        # Get student name and score
        studName = input(f"Enter student {stud+1} name: \n").title()
        studScore = int(input(f"Enter {studName}'s score: \n"))

        # #Store all student data in a list of dictionaries, e.g.
        studRecord = {
            "name": studName,
            "score": studScore,
            "grade": ""
        }
        gradeList.append(studRecord)

    # Create a function called get_grade(score) that returns a letter grade based on scale:
    def get_grade(score):
        grade = ""
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        return grade

    # Print each student’s name, score, and corresponding grade.
    # 1. Get student grade appended to list
    for stud in range(numStud):
        gradeList[stud]["grade"] = get_grade(gradeList[stud]["score"])

    # Print break out line
    print("="*50)
    print("\n\n")

    # Print out student result
    def allResult(gradeList):
        print("Name", end="\t")
        print("Score", end="\t")
        print("Grade")

        # Loop through the list and get student info
        for stud in range(len(gradeList)):
            print(gradeList[stud]["name"], end="\t")
            print(gradeList[stud]["score"], end="\t")
            print(gradeList[stud]["grade"])

    # Call function to print out students record
    allResult(gradeList)

    # Get all scores in the record then calculate Average score, highest and lowest score
    def recordScore(gradeList):
        totalScore = 0
        sortedScore = []
        top_student_list = []

        # Calculate sum of all scores
        for stud in range(numStud):
            allScores.append(gradeList[stud]["score"])
            totalScore += gradeList[stud]["score"]

        # Calculate the average score of the student
        avgScore = totalScore/numStud

        # Get Max and Min of all scores
        sortedScore = sorted(allScores)
        maxScore = sortedScore[-1]
        minScore = sortedScore[0]

        # Get the name(s) of the top student(s)
        def top_student():
            for stud in range(numStud):
                if gradeList[stud]["score"] == maxScore:
                    top_student_list.append(gradeList[stud]["name"])

        # Call top performing student function
        top_student()

        # print the average score, highest score and lowest score
        print(f"Average Score ---> {avgScore}")
        print(f"Highest Score ---> {maxScore}")
        print(f"Lowest Score ---> {minScore}")

        # Print break out line
        print("="*50)
        print("\n\n")

        # Print top student
        print("The top performing student is/are:\n")
        for top in range(len(top_student_list)):
            print(f"{top+1} --> {top_student_list[top]}")

    # Call function to print score records
    recordScore(gradeList)

    # Print break out line
    print("="*50)
    print("\n\n")

except TypeError:
    print("You inputed a wrong data type, restart program")
except ValueError:
    print("You inputed a wrong value, restart program")
finally:
    print("Thank you for using this program")
