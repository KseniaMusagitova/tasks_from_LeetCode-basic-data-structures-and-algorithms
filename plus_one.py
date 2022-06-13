
class Solution(object):
    def plusOne(self, digits):
        plus_one = int(''.join(map(str, digits))) + 1
        result = []
        while plus_one > 0:
            result.append(plus_one % 10)
            plus_one //= 10

        result.reverse()
        return result


sol = Solution()
print(sol.plusOne([1,2,3]))