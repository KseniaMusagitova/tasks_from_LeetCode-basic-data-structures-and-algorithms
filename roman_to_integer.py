
class Solution(object):
    def romanToInt(self, s):

        roman_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = list(s)

        i = 0
        result = 0
        a = 0

        while i < len(s):
            if s[i] in [key for key in roman_list]:
                if i != len(s) - 1:

                    if roman_list[s[i]] < roman_list[s[i + 1]]:
                        a = roman_list[s[i + 1]] - roman_list[s[i]]
                        i += 1

                    else:
                        a = roman_list[s[i]]

                else:
                    if roman_list[s[i]] > roman_list[s[i-1]]:
                        a = roman_list[s[i]] - roman_list[s[i-1]]
                        i += 1

                    else:
                        a = roman_list[s[i]]
            i += 1
            result = result + a
        return result


sol = Solution()
print(sol.romanToInt('XXI'))

