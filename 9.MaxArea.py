#finding conatainer with most water. leetcode problem n0. = 11
class Solution():
    def maxArea(self, height):
        left = 0
        right =len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            lenght = min(height[left], height[right])
            curr_area = width * lenght
            max_area = max(max_area, curr_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
object = Solution()
height = [1,8,6,2,5,4,8,3,7]
result = object.maxArea(height)
print(result)

            
