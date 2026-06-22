class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ayset=set()
        for num in nums:
            if num in ayset:
                return True
            ayset.add(num)
             
        return False 