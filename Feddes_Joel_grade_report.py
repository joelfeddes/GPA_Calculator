#Joel Feddes
#This program will determine your GPA, credit hours, and quality points per semester. Also, it will tell you what your final quality points, credit hours, and gpa is.
#This program will also tell you if you finished with honors overall, or if you were on the dean's list for a particular semester.
''' gpa is calculated by summing up the quality points of every course you took and then divided by the number of credit hours.
The quality points of a course is the number of credit hours multiplied by the grade numbers (an A is equal to 4).
So if I got an A in this course, I would gain 12 quality points
'''

def report_welcome():
    print("*" * 65)
    print("Grade Report Tool".center(65))
    print("*" * 65)

def find_quality_points_for_course(letter_grade,credit_hours):
    if letter_grade == "A":
        points = 4
    elif letter_grade == "A-":
        points = 3.7
    elif letter_grade == "B+":
        points = 3.3
    elif letter_grade == "B":
        points = 3
    elif letter_grade == "B-":
        points = 2.7
    elif letter_grade == "C+":
        points = 2.3
    elif letter_grade == "C":
        points = 2
    elif letter_grade == "C-":
        points = 1.7
    elif letter_grade == "D+":
        points = 1.3
    elif letter_grade == "D":
        points = 1
    elif letter_grade == "D-":
        points = 0.7
    else:
        points = 0
    contribution = points * credit_hours
    return contribution
#main
report_welcome()

fname = input("\nEnter the name of your GPA file: ")
fvar = open(fname, "r")

semester_gpa = 0 #gpa for the entire semester.
semester_hours = 0 # Credit hours achieved for the entire semester.
semester_q_points = 0 #Quality points for the entire semester
total_gpa = 0 # Final gpa
total_hours = 0 # Total credit hours taken
total_q_points = 0 # Total quality points achieved

print("\nHere is your grade summary:\n ")
print("%-15s%10s%10s%10s%20s" % ("Semester", "Hours", "Points", "GPA", "Standing"))
print("-" * 65)

for line in fvar:
    line = line.strip()
    if line == "" and semester_gpa >= 3.5: #this is telling the program what to do when we reach a new line on the list. And providing a semester gpa condition
        print("%-15s%10d%10.2f%10.2f%20s" % (semester,semester_hours,semester_q_points,semester_gpa, "DEAN'S LIST"))
        total_hours = total_hours + semester_hours
        total_q_points = total_q_points + semester_q_points
        total_gpa = total_q_points / total_hours

    elif line == "" and semester_gpa < 3.5: #this is telling the program what to do when we reach a new line on the list. And providing a semester gpa condition
        print("%-15s%10d%10.2f%10.2f" % (semester,semester_hours,semester_q_points,semester_gpa))
        total_hours = total_hours + semester_hours
        total_q_points = total_q_points + semester_q_points
        total_gpa = total_q_points / total_hours
    else: #This will split the juicy part of the text into a tab-seperated list.
        parts = line.split("\t")
        if len(parts) == 2: #This line has the semester period in it at position [1].
            semester = parts[1].upper()
            semester_gpa = 0 #reset gpa to 0
            semester_hours = 0 # reset credit hours to 0
            semester_q_points = 0 # reset quality points to 0
        
        else: #Here, I designate which position correlates to what kind of data as well as use mathy things to calculate ungiven data; like quality points.
            num_course = parts[0] 
            course_name = parts[1]
            hours = int(parts[2])
            letter_grade = parts[3]
            q_points = find_quality_points_for_course(letter_grade,hours) 
            semester_hours = semester_hours + hours
            semester_q_points = semester_q_points + q_points
            semester_gpa = semester_q_points / semester_hours
           
if semester_gpa >= 3.5: #This is the code that will activate if you have a big-ball gpa during the given semester.
    total_hours = total_hours + semester_hours
    total_q_points = total_q_points + semester_q_points
    total_gpa = total_q_points / total_hours
    print("%-15s%10d%10.2f%10.2f%20s" % (semester,semester_hours,semester_q_points,semester_gpa, "DEAN'S LIST"))
        
else: #This code will be actived if you decide to have a relaxing semester.
    total_hours = total_hours + semester_hours
    total_q_points = total_q_points + semester_q_points
    total_gpa = total_q_points / total_hours
    print("%-15s%10d%10.2f%10.2f" % (semester,semester_hours,semester_q_points,semester_gpa))
    
print("-" * 65)

if total_gpa >= 3.5: #This code will calculate your results IF your final gpa was big-baller status.
    print("%-15s%10d%10.2f%10.2f%20s" % ("Cumulative",total_hours,total_q_points,total_gpa,"HONORS"))
    
else: #This code will calculate your results IF your final gpa reflects your study habits.
    print("%-15s%10d%10.2f%10.2f" % ("Cumulative",total_hours,total_q_points,total_gpa))

input("\nPress enter to exit program")
            
fvar.close()


    
                


















        
