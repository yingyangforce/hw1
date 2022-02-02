# File: grace_hw1a.py
# Author: Isaiah Grace
# Date: 22/2/2
# Section: Tuesday lab
# E-mail: isaiah.grace@maine.edu
# Description: Tax adder
# Collabs: N/a

print("\nWelcome to the Computer Store!\n")

cost = int(input("How much do you want to spend? "))

total_cost = cost + (cost * .06) # add 6% tax

print(f"\nYou will actually spend ${total_cost}\n")

print("Are you sure you want to do that?")
