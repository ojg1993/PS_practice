class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        equations = [["a","b"],["b","c"]]
        values = [2.0,3.0] -> [a/b, b/c]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

        if query variable does not exist in equations, return -1
        a -> b = 2    b -> c = 3
        b -> a = 1/2  c -> b = 1/3
        hash = {a : [[b, a/b]] , b:[[a, b/a]] ...}
        """

        graph = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def bfs(cur, target):
            if cur not in graph or target not in graph:
                return -1
            q, visit = deque(), set()
            q.append((cur, 1))
            visit.add(cur)

            while q:
                n, w = q.popleft()
                if n == target:
                    return w

                for nei in graph[n]:
                    node, weight = nei
                    if node not in visit:
                        q.append((node, w * weight))
                        visit.add(node)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
