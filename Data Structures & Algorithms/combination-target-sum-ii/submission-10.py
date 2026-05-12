class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        nums=sorted(candidates)

        def dfs(i,subset,total):
            if total==target:
                res.append(subset.copy())
                return

            if i>=len(nums) or total>target:
                return

            subset.append(nums[i])
            dfs(i+1,subset,total+nums[i])

            subset.pop()
            while i+1 <len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,subset,total)

        dfs(0,[],0)
        return res