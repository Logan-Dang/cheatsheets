# Cheatsheet 2: Decisions and if statements in Python

# If statements in Python

# If statements are used to make decisions in Python
# They allow you to execute a block of code only if a certain condition is met
# The basic syntax is:
# if condition:
#     code to execute if condition is True
# elif another_condition:
#     code to execute if another_condition is True
# else:
#     code to execute if none of the above conditions are True

# These are useful when you can reframe your problem as a series of yes/no questions
# For example, you can ask if a number is positive or negative by asking 3 questions:
# 1. Is the number greater than 0?
# 2. Is the number less than 0?
# 3. Is the number equal to 0?


num = 42 # Set the variable num to the value 42
if num > 0: # If the variable num is greater than 0
    print("Positive") # Print "Positive"
elif num < 0:
    print("Negative")
else:
    print("Zero")
# Try changing the value of num to see how the output changes

# The ordering of your if/elifs statements matters
# The first condition that evaluates to True will execute its block of code
# The rest will be ignored

grade = 85 # Set the variable grade to the value 85
if grade >= 90: # If the variable grade is greater than or equal to 90
    print("A") # Print "A"
elif grade >= 80: # Else if... so on and so forth
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
# Try changing the value of grade to see how the output changes

# Just like English, the same thing can be said in many different ways
if grade < 60: # If the variable grade is less than 60
    print("F") # Print "F"
elif grade < 70:
    print("D")
elif grade < 80:
    print("C")
elif grade < 90:
    print("B")
else:
    print("A")
# The above code is equivalent to the previous example, but uses different conditions
# Try changing the value of grade to see how the output changes, but note that the same grade will print twice each time