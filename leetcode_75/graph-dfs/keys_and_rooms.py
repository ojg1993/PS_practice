class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room):
            visit.add(room)
            for key in rooms[room]:
                if key not in visit:
                    dfs(key)
        visit = set()
        dfs(0)
        return len(rooms) == len(visit)
