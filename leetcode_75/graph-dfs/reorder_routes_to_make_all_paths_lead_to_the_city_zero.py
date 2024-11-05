class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        def dfs(origin):
            nonlocal res, visit
            for nei in graph[origin]:
                if nei not in visit:
                    if (nei, origin) not in edges:
                        res += 1
                    visit.add(nei)
                    dfs(nei)

        edges = {(s, e) for s, e in connections}
        graph = defaultdict(list)
        for s, e in connections:
            graph[s].append(e)
            graph[e].append(s)

        res, visit = 0, set([0])
        dfs(0)
        return res
