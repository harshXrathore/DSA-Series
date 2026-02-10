class Solution:
    def twoSum(self, nums, target):
        seen = {}
        
        for i,num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i

nums = [5, 2, 11, 7, 5]
target = 9

obj = Solution()
result = obj.twoSum(nums, target)
print(result)
