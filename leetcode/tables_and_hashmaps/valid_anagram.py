from typing import List

# O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for char in s:
            hash_s[char] = hash_s.setdefault(char, 0) + 1
        for char in t:
            hash_t[char] = hash_t.setdefault(char, 0) + 1
        return hash_s == hash_t