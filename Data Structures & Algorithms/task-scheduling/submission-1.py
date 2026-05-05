class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        counts=Counter(tasks)
        maxHeap=[-s for s in counts.values()]
        heapq.heapify(maxHeap)
        q=deque()
        print(f"counts: {counts}")
        print(f"maxHeap: {maxHeap}")
        print(f"deq: {q}")

        while maxHeap or q:
            time+=1
            if maxHeap:
                num=1+heapq.heappop(maxHeap)
                if num:
                    q.append([num,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time