class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReq = { i:[] for i in range(numCourses)}
        # [0,1]
        # 0: [1]

        for i,j in prerequisites:
            preReq[i].append(j)

        visited = set()
        visiting = set()

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
            return True


        sol = True
        for i in range(numCourses):
            sol = sol and dfs(i)
        return sol
        
        