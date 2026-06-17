class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=defaultdict(list)
        for prereq in prerequisites:
            preMap[prereq[0]].append(prereq[1])
        print(f"preMap:{preMap}")
        visited_set=set()

        def dfs(crs):
            if preMap[crs]==[]:
                return True
            if crs in visited_set:
                print(f"crs:{crs} is in visited_set")
                return False
            visited_set.add(crs)
            
            for reqs in preMap[crs]:    
                print(f"crs:{crs} | preMap[crs]:{preMap[crs]} | reqs:{reqs}")
                if not dfs(reqs):
                    return False
            preMap[crs]=[]
            visited_set.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True