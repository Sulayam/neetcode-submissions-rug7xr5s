class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        arr= [[] for n in range(len(nums)+1)]
        for i in range(len(nums)):
            hashmap[nums[i]]=1+hashmap.get(nums[i],0)

        for i, n in enumerate(hashmap):
            arr[hashmap.get(n,0)].append(n)
        
        final=[]
        for i in range(len(arr)-1,0,-1):
            for element in arr[i]:
                final.append(element)
                if len(final)==k:
                    return final