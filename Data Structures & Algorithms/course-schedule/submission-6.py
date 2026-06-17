class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=defaultdict(list)
        for req in prerequisites:
            preMap[req[0]].append(req[1])
        visited_set=set()
        print(f"preMap: {preMap}")
        
        def dfs(cur):
            if preMap[cur]==[] or cur not in preMap:
                return True
            if cur in visited_set:
                print(f"cur: {cur}")
                print(f"visited_set: {visited_set}")
                return False
            visited_set.add(cur)
            for req in preMap[cur]:
                print(f"preMap[cur]: {preMap[cur]}")
                print(f"req: {req}")
                if not dfs(req):    
                    return False
            visited_set.remove(cur)
            preMap[cur]=[]
            return True

        for cur in range(numCourses):
            if not dfs(cur):
                
                return False
        return True