# Median of Two Sorted Arrays 
# LeetCode - https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

nums1 = [1,3]
nums2 = [2,4]

# create an empty list for merger 
temp_L = []

# using extend function to merge both the lists
temp_L.extend(nums1)
temp_L.extend(nums2)

# now sort the list
temp_L.sort()

# find the size of the list
size_L = len(temp_L)

print("Median: ", end="")
# check if the List is even or odd in size
if size_L % 2 == 0: 
    element = size_L // 2 
    # since the list is even median will be mean of two center elements
    print(float((temp_L[element - 1] +temp_L[element])/2))
else:
    element = size_L // 2
    print(float(temp_L[element]))


# 💡 Python has two division operators : 
# /: divides the number on left by right and returns float value
# //: divides the number on left by right and rounds the return value