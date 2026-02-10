class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        s = set()
        ans = []
        actualSum = 0
        
        for i in range(n):
            for j in range(n):
                actualSum += grid[i][j]
                if grid[i][j] in s:
                    a = grid[i][j]
                    ans.append(a)
                else:
                    s.add(grid[i][j])
        
        expSum = (n * n) * (n * n + 1) // 2
        b = expSum + a - actualSum
        ans.append(b)
        
        return ans

obj = Solution()
grid = [[1,3],[2,2]]

result = obj.findMissingAndRepeatedValues(grid)
print(result)
    
        
        
