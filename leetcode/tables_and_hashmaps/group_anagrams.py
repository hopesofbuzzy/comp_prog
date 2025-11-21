from typing import List

# O(n*m) n - len(strs), m - len(s)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_groups = {}
        for s in strs:
            list_s = [0] * 26
            for char in s:
                list_s[ord(char)-ord('a')] += 1
            tuple_s = tuple(list_s)
            hash_groups[tuple_s] = hash_groups.setdefault(tuple_s, []) + [s]

        return [[s for s in hash_groups[key]] for key in hash_groups]