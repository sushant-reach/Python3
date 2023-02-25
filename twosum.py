class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i 


Sol = Solution()

ns = [11,15,2,7,11,15]
tgt = 9

x=Sol.twoSum(ns,tgt)

for i, value1 in enumerate(x):
    print(value1)



