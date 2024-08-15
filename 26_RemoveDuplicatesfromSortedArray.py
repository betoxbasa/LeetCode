from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):                        
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

#Parameters for testcase
nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1,1,2]
print(nums)
a = Solution()
k= a.removeDuplicates(nums)
print("after method")
print(k)
print(nums)
