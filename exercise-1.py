"""
Exercise 1
"""

# PART 1: Gather Information

# IndexError: list index out of range
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# The expected output is 4. The actual output is a error message.
# - What error message (if any) is there?

# Here is the stack trace we get from running the program:
# Traceback (most recent call last):
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-1.py", line 49, in <module>
#     answer = find_largest_diff([5, 3, 1, 2, 6, 4])
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-1.py", line 42, in find_largest_diff
#     diff = abs(list_of_nums[i] - list_of_nums[i+1])

# - What line number is causing the error?
# Line 49, and line 42.

# - What can you deduce about the cause of the error?
# The error is caused by the index out of range.
# The first thing we do is to initiate the largest_diff variable to 0 and print out the change in every iteration.
# Next we got the result and see that the loop went through the list but stopped at the last iteration.
# The loop stopped at the last iteration because the code - diff = abs(list_of_nums[i] - list_of_nums[i+1]) - is not executed.
# If i get to the last iteration, i will point to the last element. That means i+1 will create an index out of range error.

# Conclusion:
# We need to adjust the for loop to let i stop before the last element.

# PART 2: State Assumptions

# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)-1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff
    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)
