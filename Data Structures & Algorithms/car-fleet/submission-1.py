class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        pairs.sort()
        pairs.reverse()
        
        # time=target-p/s
        
        print(f"pairs:{pairs}")
        for p, s in pairs:
            stack.append((target-p)/s)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
