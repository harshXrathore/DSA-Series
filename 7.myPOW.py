class Solution:
    def myPOW(self, x, n):
        result = 1
        if n < 0:
            x = 1/x
            n = -n
        while n > 0:
            if n % 2 == 1:
                result = result * x
            x = x * x
            n //= 2
        return result

object = Solution()
x = 2.00000
n = 10
ans = object.myPOW(x, n)
print(ans)
            
