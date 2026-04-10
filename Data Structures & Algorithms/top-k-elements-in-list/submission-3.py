class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        print(f"len(nums):{len(nums)}")
        arr= [[] for n in range(len(nums)+1)]
        print(f"arr:{arr}")
        for number in nums:
            hashmap[number]=1+hashmap.get(number,0)
        print(f"hashmap:{hashmap}\n")

        for i, n in enumerate(hashmap):
            print(f"i->{i}\t key->{n} value->{hashmap.get(n,0)}\n")
            arr[hashmap.get(n,0)].append(n)
        print(f"new arr:{arr}")
        
        final=[]
        for i in range(len(arr)-1,0,-1):
            for element in arr[i]:
                final.append(element)
                if len(final)==k:
                    print(f"final :{final}")
                    return final