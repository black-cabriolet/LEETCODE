"""The problem you're solving, often called the "Two Sum" problem, is a classic algorithmic problem in computer science. Here's an explanation:

Problem Statement: Given an array of integers nums and an integer target, you need to find two numbers in the array such that their sum equals the target. You must return the indices of these two numbers.

Assumptions:

1 Each input will have exactly one solution.
2 You cannot use the same element (number) twice to form the sum.
Example:
Let's take an example with the input array nums = [2, 7, 11, 15] and target = 9. We need to find two numbers in nums whose sum is equal to target, which is 9.

First, we start iterating through the array. The first number is 2.
We calculate the complement needed to reach the target: complement = target - num = 9 - 2 = 7.
We check if this complement (7) is already in our dictionary of number indices. Since it's not, we add the current number (2) and its index (0) to the dictionary.
Next, we move to the next number (7) in the array.
Again, we calculate the complement: complement = target - num = 9 - 7 = 2.
Now, we find that this complement (2) exists in our dictionary with index 0. This means the numbers at indices 0 and 1 (2 and 7) add up to the target (9).
So, the function should return [0, 1], which are the indices of the numbers 2 and 7 that add up to 9.

The algorithm works similarly for other input cases. It efficiently uses a dictionary to store the indices of numbers encountered so far, making it possible to find the solution in linear time complexity O(n), where n is the number of elements in the input array nums."""


class Solution(object):
    def twoSum(self, nums, target):
        num_indices = {}  # Dictionary to store each number and its index
        for i, num in enumerate(nums):
            complement = (
                target - num
            )  # Calculate the complement needed to reach the target
            if complement in num_indices:
                # If complement exists in the dictionary, return its index along with the current index
                return [num_indices[complement], i]
            # Add the current number and its index to the dictionary
            num_indices[num] = i
        # If no solution is found, return an empty list or raise an exception
        return []


# Example usage:
solution = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
