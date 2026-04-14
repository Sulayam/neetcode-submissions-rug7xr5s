class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R=0,0
        hashset=set()
        res=0

        while R<len(s):
            while s[R] in hashset:
                hashset.remove(s[L])
                L=L+1
            hashset.add(s[R])
            R=R+1
            res = max(res, len(hashset))
        return res