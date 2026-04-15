class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT,window={},{}
        res = (-1,-1)
        resLen = float('infinity')
        l=0
        
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        # print(f"len(countT):{len(countT)}")
        have,need=0,len(countT)

        for r in range(len(s)):
            c=s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c]==countT[c]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    resLen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT.get(s[l],0):
                    have-=1  
                l+=1
        l,r=res
        return s[l:r+1] if resLen != float('infinity') else ""