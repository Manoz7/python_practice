'''
Problem Statement

You are given a sorted array of integers and a target value.

Return the indices (1-based) of the two numbers such that they add up to the target.

Each input has exactly one solution
You cannot use the same element twice
You must use constant extra space
'''

def two_sum(arr, target):

    left = 0
    right = len(arr)-1

    while left < right:

        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            return left, right

        elif curr_sum <target:
            left +=1
        
        else: 
            right -=1
    
arr = [1, 5, 9, 11, 20]
target = 20


print("Two indices are: ", two_sum(arr, target))
