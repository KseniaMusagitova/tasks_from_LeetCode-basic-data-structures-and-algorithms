class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = ''.join(i for i in s if i.isalnum())
        return s.lower()[::-1] == s.lower()


sol = Solution()
print(sol.isPalindrome(s = "0P"))

