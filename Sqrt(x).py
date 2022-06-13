
class Solution(object):
    def mySqrt(self, x):

        from math import sqrt
        a = sqrt(x)
        b = a * 100 // 100
        b = int(b / 1)
        return b


sol = Solution()
print(sol.mySqrt(8))

