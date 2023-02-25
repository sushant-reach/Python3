class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
         num1 = [0,1,1,0]
         num2 = [1,2,2,5]
         temp  = [num1, num2]
         return temp     

sol=Solution()
nums = [0,1,2,3,4]
a=sol.threeSum(nums)
print(a)
