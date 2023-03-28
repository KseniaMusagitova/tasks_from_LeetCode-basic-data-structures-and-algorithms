from typing import List
import pytest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_words = {}
        for word in strs:
            sorted_tuple = tuple(sorted(word))
            if sorted_tuple in tuple_words:
                tuple_words[sorted_tuple].append(word)
            else:
                tuple_words[sorted_tuple] = [word, ]
        return list(tuple_words.values())


s = Solution()

@pytest.mark.parametrize("strs, answer", [
    (["eat","tea","tan","ate","nat","bat"],
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
    ])


def test_solution(strs, answer):
    assert s.groupAnagrams(strs) == answer



