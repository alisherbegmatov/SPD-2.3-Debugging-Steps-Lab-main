"""
Exercise 2
"""

# PART 1: Gather Information

# TODO: Gather information about the source of the error and paste your findings here. E.g.:

# - What is the expected vs. the actual output?
# The expected output should be False, True. The actual output is False, False.

# - What error message (if any) is there?
# No error message.

# - What line number is causing the error?
# No error message.

# - What can you deduce about the cause of the error?
# The error is caused by wrong if/else statement logic. If the fisrt 3 numbers are not consecutive, the code will always return False.
# To prove this assumption, we can call the function by passing the list [1, 2, 3, 5] and see that it returns True.

# Connclusions:
# We just need to remove the else statement and it will only return False after the for loop iterates through the list and did not find any 3-consecutive numbers.

# PART 2: State Assumptions

# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True

    # answer3 = contains_3_consecutive([1, 2, 3, 5])
    # print(answer3) # should print True
