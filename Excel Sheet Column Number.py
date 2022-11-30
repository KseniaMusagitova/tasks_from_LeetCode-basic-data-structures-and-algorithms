# option 1
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for i in range(len(columnTitle)):
            result = result * 26 + (ord(columnTitle[i]) - ord('A') + 1)
        return result


sol = Solution()
print(sol.titleToNumber("ABD"))


# option 2
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for i in range(len(columnTitle)):
            res = (res * 26) + (ord(columnTitle[i]) - 64)
        return res


sol = Solution()
print(sol.titleToNumber("ABD"))