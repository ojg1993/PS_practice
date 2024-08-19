class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map graph
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        # define dfs
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)

            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        # call dfs
        res = []
        visit, cycle = set(), set()
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
