class Solution():
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        idx = m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1
        
        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1
        return nums1 

obj = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
result = obj.merge(nums1, m, nums2, n)
print(result)
 
