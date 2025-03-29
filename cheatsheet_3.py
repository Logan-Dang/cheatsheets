# Cheatsheet 3: Loops in Python

# Loops are used to repeat a block of code multiple times
# There are two main types of loops in Python: for loops and while loops

# While loops are used to repeat a block of code as long as a certain condition is True
# The basic syntax is:
# while condition:
#     code to execute while condition is True
# else:
#     code to execute once the condition is False
#
# The else block is optional and rarely used

# For example, you can use a while loop to print the numbers from 1 to 10:
num = 1 # Set the variable num to the value 1
while num <= 10: # While the variable num is less than or equal to 10
    print(num) # Print the value of num
    num += 1 # Increase num by 1
    # This is equivalent to num = num + 1 and is seen as a shorter way to write it

# For loops are used to iterate over a sequence (like a list, tuple, or string)
# The basic syntax is:
# for item in sequence:
#     code to execute for each item in the sequence
# else:
#     code to execute once the loop is finished
# The else block is optional and rarely used

# For example, you can use a for loop to print the numbers from 1 to 10:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Set the variable nums to the list of numbers from 1 to 10
for digit in digits: # For each digit in the list of digits
    print(digit) # Print the value of digit
    
# Note that although the two loops above produce the same output, they are not equivalent
# The while loop is like saying "do this until num is not less than or equal to 10 (aka greater than 10)"
# The for loop is like saying "do this for each digit in the list of digits"
# Just like in English, sometimes two wildly different sentences can mean the same thing

# The for loop will generally be useful when you have a sequence or can easily create one
# The while loop is useful when you want to repeat a block of code until a certain condition is met

# You can also use the break statement to exit a loop early
new_num = 5
while True: # True is always True, so "forever,"
  if new_num == 0: # If new_num is equal to 0
    break # Exit the loop
  print(new_num) # Print the value of new_num
  new_num -= 1 # Decrease new_num by 1
  # This is equivalent to new_num = new_num - 1
  
# Forever, check if new_num is equal to 0
# If it is, exit the loop
# If it isn't, print the value of new_num and decrease it by 1

l = list(range(10)) # Set the variable l to a list of numbers from 0 to 9
# Notice how there is no pretty way to say "a list of numbers from 0 to 9" in English
# This is why we call it Jargonese
for i in l: # For each i in the list l
    if i == 5: # If i is equal to 5
        break # Exit the loop
    print(i) # Print the value of i

# Fun fact: we chose the term break because of how we often say "break the cycle" in English
# You can also use the continue statement to skip the rest of the loop and go to the next iteration

# For example, you can use the continue statement to skip the number 5:
for i in range(10): # For each i in the "list" of numbers from 0 to 9
    if i == 5: # If i is equal to 5
        continue # Skip the rest of the loop and go to the next iteration
    print(i) # Print the value of i