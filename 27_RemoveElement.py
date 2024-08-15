# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if val == nums[i] :                 
                nums[i] = 51
            else :
                k+=1

        nums.sort()        
        return k

#Parameters for testcase
nums = [0,1,2,2,3,0,4,2]
val = 2

print(nums)
a = Solution()
k= a.removeElement(nums, val)
print(k)
print(nums)
