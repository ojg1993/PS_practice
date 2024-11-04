class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(cur):
            visit.add(cur)
            for nei in range(len(isConnected[cur])):
                if isConnected[cur][nei] and nei not in visit:
                    dfs(nei)

        res, visit = 0, set()
        for i in range(len(isConnected)):
            if i not in visit:
                res += 1
                dfs(i)
        return res