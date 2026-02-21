class Solution:
    def singleNumber(self, nums):
        ans = 0
        for i in  nums:
            ans = ans ^ i 
        return ans

obj = Solution()
nums = [4,1,2,1,2]
result = obj.singleNumber(nums)
print(result)
