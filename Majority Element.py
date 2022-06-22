class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m_element = {}
        for i in nums:
            m_element[i] = m_element.get(i, 0) + 1
        return max(m_element.items(), key=lambda x: (x[1], x[0]))[0]



sol = Solution()
print(sol.majorityElement(nums = [3,2,3,4,4,4]))