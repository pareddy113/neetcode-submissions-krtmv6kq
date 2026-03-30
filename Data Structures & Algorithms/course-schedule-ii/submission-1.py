class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preReq = { i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            preReq[j].append(i)

        visiting = set()
        visited = set()
        res = []

        def dfs(course):

            if course in visiting:
                return False
        
            if course in visited:
                return True
                
            visiting.add(course)

            for i in preReq[course]:
                if not dfs(i):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]
        
        