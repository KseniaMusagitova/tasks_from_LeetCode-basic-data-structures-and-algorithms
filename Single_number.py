class Solution(object):
    def singleNumber(self, nums):

        only_one = []

        for i in nums:
            if i in only_one:
                only_one.remove(i)
            else:
                only_one.append(i)

        return int(str(only_one[0]).replace(",", ""))


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))