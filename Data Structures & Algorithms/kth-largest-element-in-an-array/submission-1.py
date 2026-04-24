class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[-num for num in nums]
        heapq.heapify(minHeap)

        while k>0:
            k-=1
            x=heapq.heappop(minHeap)
            if k==0:
                return -x
        return 0