class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([(entrance[0], entrance[1], 0)])
        visit = set([(entrance[0], entrance[1])])
        while q:
            y, x, cnt = q.popleft()

            for yy, xx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 <= yy < len(maze) and 0 <= xx < len(maze[0]) and (yy, xx) not in visit and maze[yy][xx] == ".":
                    if yy in [0, len(maze)-1] or xx in [0, len(maze[0])-1]:
                        return cnt+1
                    visit.add((yy, xx))
                    q.append((yy, xx, cnt+1))
        return -1
