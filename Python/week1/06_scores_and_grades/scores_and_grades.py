#Create a program that prompts the user ten times for a test score between 60
#and 100. Each time a score is generated, your program should display what the
#grade is for a particular score. Here is the grade table:

#Score: 60 - 69; Grade - D
#Score: 70 - 79; Grade - C
#Score: 80 - 89; Grade - B
#Score: 90 - 100; Grade - A

#The result should be like this...
#Scores and Grades
#Score: 87; Your grade is B
#Score: 67; Your grade is D
#Score: 95; Your grade is A
#Score: 100; Your grade is A
#Score: 75; Your grade is C
#Score: 90; Your grade is A
#Score: 89; Your grade is B
#Score: 72; Your grade is C
#Score: 60; Your grade is D
#Score: 98; Your grade is A
#End of the program. Bye!

grades = []

def prompt():
    for i in range(10):
        score = raw_input("Please enter test score between 60 and 100: ")
        grades.append(score)

def results(grades):
    for i in range(0,len(grades)):
        if int(grades[i]) > 100:
            print "Score: " + grades[i] + "; This is not a valid test score."
        elif int(grades[i]) > 89:
            print "Score: " + grades[i] + "; Your grade is A"
        elif int(grades[i]) > 79:
            print "Score: " + grades[i] + "; Your grade is B"
        elif int(grades[i]) > 69:
            print "Score: " + grades[i] + "; Your grade is C"
        elif int(grades[i]) > 59:
            print "Score: " + grades[i] + "; Your grade is D"
        else:
            print "Score: " + grades[i] + "; This is not a valid test score."


prompt()
print "Scores and Grades"
results(grades)
print "End of the program. Bye!"
