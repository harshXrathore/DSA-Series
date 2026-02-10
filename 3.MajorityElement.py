class Solution(object):
    def majorityElement(self, nums):
         freq = 0
         ans = 0
         for i in range(0, len(nums)):
             if freq == 0:
                 ans = nums[i]
             if ans == nums[i]:
                 freq +=1
             else:
                 freq -= 1
         return ans     
                       
nums = [1,2,1,2,3,1,1,1,1,2,1,1]

obj = Solution()
result = obj.majorityElement(nums)
print(result)
                
