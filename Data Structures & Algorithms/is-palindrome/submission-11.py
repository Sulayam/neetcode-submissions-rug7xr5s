class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            print(f" l:{l}\t s[l]:{s[l]}\n r:{r}\t s[r]:{s[r]}")
            while l<r and not self.isAlphaNumber(s[l]):
                l+=1
            while l<r and not self.isAlphaNumber(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            r-=1
            l+=1
        return True


    def isAlphaNumber(self, c) -> bool:
        return (ord('A')<=ord(c)<=ord('Z')
            or ord('a')<=ord(c)<=ord('z')
            or ord('0')<=ord(c)<=ord('9'))