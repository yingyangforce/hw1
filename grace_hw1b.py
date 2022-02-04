# File: grace_hw1b.py
# Author: Isaiah Grace
# Date: 22/2/2
# Section: Tuesday lab
# E-mail: isaiah.grace@maine.edu
# Description: Weighted average calculator
# Collabs: N/a

# Weights used for calculations - 
# ---
# HW       - 30%
# Projects - 20%
# Exams    - 35%
# Labs     - 10%
# Pro Dev  - 5%


hw = float(input("Enter your homework average: "))

projects = float(input("Enter your project average: "))

labs = float(input("Enter your lab average: "))

prodev = float(input("Enter your professional development average: "))

exams = float(input("Enter your exam average: "))

weighted_avg = (hw * .3) + (projects * .2) + (exams * .35) + (labs * .1) + (prodev * .05)

print(f"Your weighted average grade is: {weighted_avg}")
