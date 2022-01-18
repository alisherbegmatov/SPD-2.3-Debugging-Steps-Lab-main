"""
Exercise 3
"""

# PART 1: Gather Information

# TODO: Gather information about the source of the error and paste your findings here. E.g.:

# - What is the expected vs. the actual output?
# The expected output is [1,2,3,5,6] and the actual output is error message.

# - What error message (if any) is there?
# Traceback (most recent call last):
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-3.py", line 34, in <module>
#     answer = insertion_sort([5, 2, 3, 1, 6])
#   File "/Users/alisherbegmatov/Documents/Code/Make School/Semester 2/ACS 4931 - SPD 2.31/SPD-2.3-Debugging-Steps-Lab-main/exercise-3.py", line 26, in insertion_sort
#     while key < arr[j] : 
# IndexError: list index out of range

# - What line number is causing the error?
# Line 34, and line 26.

# - What can you deduce about the cause of the error?
# Finst we assign j to i-1 and we print out how j will change before and after the while loop.
# Also, we found out that j-=1 will make j to be negative and it will cause an index out of range error.

# Conclusion:
# We need to adjust the while loop to let j stop if it turns negative, so we change the while loop to: while j>=0 and key < arr[j] : 

# PART 2: State Assumptions

# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while j>=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)
