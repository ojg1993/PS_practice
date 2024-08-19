class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if not graph[crs]:
                return True
            cycle.add(crs)

            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            graph[crs] = []
            return True

        cycle = set()
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
