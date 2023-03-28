import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        mapping = {}
        max_word_rate = 0
        max_common_word = ""
        paragraph = paragraph.lower()
        for word in re.findall(pattern=r"\w+", string=paragraph):
            if word in banned:
                continue
            if word not in mapping:
                mapping[word] = 1
            else:
                mapping[word] += 1
            if mapping[word] > max_word_rate:
                max_common_word = word
                max_word_rate = mapping[word]
        return max_common_word


sol = Solution()
print(sol.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))