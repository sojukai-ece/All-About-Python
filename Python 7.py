"""
The Challenge: The Classroom Grade Analyzer
Objective: Write a Python script that takes a predefined list of student 
test scores, manually calculates the average, finds the highest and lowest scores, 
and categorizes them into letter grades.

Step-by-Step Requirements
Setup Tracking Variables: Before looping, create variables to keep track of 
the total sum of all scores, the highest score, and the lowest score.

Hint: You can set the initial highest score to 0, and the initial lowest score to 100.

Setup Grade Counters: Create variables to count how many students got an A, B, C, or F. Set them all to 0.

The Main Loop: Create a single for loop that iterates through every score in the scores list. Inside this loop, you must:

Add the current score to your total sum.

Check if the current score is greater than your tracked highest score. If it is, update the highest score.

Check if the current score is less than your tracked lowest score. If it is, update the lowest score.

Use if, elif, and else statements to check the score's value and add 1 to the correct letter grade counter based on this scale:

A: 90 to 100

B: 80 to 89

C: 70 to 79

F: Less than 70

Calculate the Average: After the loop finishes, calculate the class average
by dividing the total sum by the number of students. (You can use the built-in len() 
function to find out how many students there are).

Print the Report: Print a final formatted report showing the total 
number of students, the class average (formatted to exactly one decimal place 
using what you learned earlier!), the highest and lowest scores, and the breakdown of letter grades.
"""

scores = [85, 92, 78, 60, 100, 73, 88, 95, 45, 82]

total_sum = 0
highest_score = 0
lowest_score = 100

count_a = 0
count_b = 0
count_c = 0
count_f = 0

for score in scores:
    total_sum += score

    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score
    if score >= 90:
        count_a += 1 
    elif score >= 80:
        count_b += 1
    elif score >= 70:
        count_c += 1
    else:
        count_f += 1

#Summary
number_of_students = len(scores)
average = total_sum / number_of_students

print("--- Class Grade Report ---")
print(f"Total Students: {number_of_students}")
print(f"Class Average: {average:.1f}") 
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}\n")

print("--- Grade Distribution ---")
print(f"A (90-100): {count_a}")
print(f"B (80-89): {count_b}")
print(f"C (70-79): {count_c}")
print(f"F (<70): {count_f}")

