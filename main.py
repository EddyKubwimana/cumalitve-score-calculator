from collections import Counter

#definition of  a function that convert grade form mark percentage out of 100 and return the letter and grade out of 4.00
def grade_converter(score):

    if score <= 100 and score >= 85:
        grade = {"A+": 4.00}
    elif score >= 80 and score < 85:
        grade = {"A": 4.00}
    elif score >= 75 and score < 80:
        grade = {"B+": 3.50}
    elif score >= 70 and score < 75:
        grade = {"B": 3.00}
    elif score >= 65 and score < 70:
        grade = {"C+": 2.50}
    elif score >= 60 and score < 65:
        grade = {"C": 2.00}
    elif score >= 55 and score < 60:
        grade = {"D+": 1.50}
    elif score >= 50 and score < 55:
        grade = {"D": 1.00}
    elif score < 50:
        grade = {"E": 0.00}
    return grade
# definition of function that take cumulative gpa and tells the user the honor she/he graduated with
def cumulative_grade(grade):
    if grade >= 3.85 and grade <= 4.0 :
        return "Summa Cum Laude"
    elif grade >= 3.7 and grade < 3.85 :
        return "Magna Cum Laude"
    elif grade >= 3.5 and grade <3.7:
        return " Cum Laude"
    else :
        return " You did not graduate with any honor"
# taking input for user for number of courses he/she is taking and creations of list that are going to holds grade and weight of a course
print( " How many course do you want to enter score for?")
number_course = int(input(">>>"))
course_grade = []
course_weight = []
# iteration that help user enter courses number she/he input above
for grade in range (1, number_course+1 ):
    print(f" what grade do you have in course{grade}")
    course_mark = float(input(">>>"))
    course_grade.append(course_mark)
    print(F"what is the weight of course {grade}")
    weight = float(input(">>>"))
    course_weight.append(weight)
course_num = 1
cumulative_gpa = []
grade_in_letter=[]

#iteration throught course grade list to find
for i in course_grade:
    #call of grade converter on each grade the user input to find the letter and grade out of 4.00
   scoring = grade_converter(i)
    #Because scoring is a dictionary, we have to unpack it to be able to find the letter and the grade out of 4 by iterating the items in it
   for key, value in scoring.items():
       print( f"course{ course_num} grade in letter is ", key , " grade out of 4.00 is ", value)
       grade_in_letter.append(key)
       cumulative = value*course_weight[course_num-1]
       cumulative_gpa.append(cumulative)

   course_num+=1
# counter of As, Bs
letter_counter = Counter(grade_in_letter)
for ke,va in letter_counter.items():
    print(f" Well done, you have {va}", f"{ke}s")

#find the total weight of all courses

sum_weight = 0
for i in course_weight:
    sum_weight = sum_weight + i
print(sum_weight)

# find the cumulative Gpa with weights applied to each course accordingly
total_grade = 0
for cu in cumulative_gpa:
    total_grade = total_grade+cu
    final_gpa = total_grade/sum_weight
print(" graduate with ", cumulative_grade(final_gpa))















