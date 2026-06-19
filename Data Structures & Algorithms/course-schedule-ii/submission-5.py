class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited_set=set()
        preMap=defaultdict(list)
        res=[]

        for req in prerequisites:
            preMap[req[0]].append(req[1])
        print(f"preMap:{preMap}")

        def dfs(crs):
            if (preMap[crs]==[]):
                res.append(crs)
                return True
            if crs in visited_set:
                return False
            visited_set.add(crs)
            
            for preReq in preMap[crs]:
                if not dfs(preReq):
                    return False
            res.append(crs)
            visited_set.remove(crs)
            preMap[crs]=[]
            return True
            
        for crs in range(numCourses):
            if dfs(crs)==False:
                return []
        final=[]
        setter=set()
        for r in res:
            if r not in setter:
                final.append(r)
            setter.add(r)

        return final