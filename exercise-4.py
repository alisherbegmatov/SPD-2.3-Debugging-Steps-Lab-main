"""
Exercise 4
"""

# PART 1: Gather Information

# TODO: Gather information about the source of the error and paste your findings here. E.g.:

# - What is the expected vs. the actual output?
# The expected output should be 4, the actual output is an error message.

# - What error message (if any) is there?
# Traceback (most recent call last):
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-4.py", line 41, in <module>
#     answer = binary_search([1, 2, 4, 5, 7], 7)
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-4.py", line 37, in binary_search
#     return binary_search(arr, element, mid, high)
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-4.py", line 37, in binary_search
#     return binary_search(arr, element, mid, high)
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-4.py", line 37, in binary_search
#     return binary_search(arr, element, mid, high)
#   [Previous line repeated 995 more times]
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-4.py", line 22, in binary_search
#     if high == None:
# RecursionError: maximum recursion depth exceeded in comparison

# - What line number is causing the error?
# Line 41, line 37, and line 22.

# - What can you deduce about the cause of the error?
# It seems that the recursion function is stuck in an infinite loop, so we first print out the mid.
# From the output of mid, we can see that it stays the same after the first iteration because we did not change the high or low variable when calling the new recursion function.

# Conclusion:
# We need to change the recursion function to:
#   elif arr[mid] > element:
#         return binary_search(arr, element, low, mid-1)

#     else: 
#         return binary_search(arr, element, mid+1, high)

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2
    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid-1)

    else: 
        return binary_search(arr, element, mid+1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)
