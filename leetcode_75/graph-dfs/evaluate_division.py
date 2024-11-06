class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def bfs(s, e):
            if s not in graph or e not in graph:
                return -1
            visit = set([s])
            q = deque([(s, 1)])

            while q:
                node, weight = q.popleft()
                if node == e:
                    return weight

                for nei, w in graph[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, weight*w))
            return -1

        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        return [bfs(s, e) for s, e in queries]
