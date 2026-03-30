class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReq = { i:[] for i in range(numCourses)}
        # [0,1]
        # 0: [1]

        for i,j in prerequisites:
            preReq[i].append(j)

        visited = set()

        def dfs(course):

            if course in visited:
                return False

            if len(preReq[course]) == 0:
                return True

            visited.add(course)

            for i in preReq[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            return True


        sol = True
        for i in range(numCourses):
            sol = sol and dfs(i)
        return sol
        
        