class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort()
        cnt = 1
        overlap = points[0]

        for i in range(1, len(points)):
            cur = points[i]

            if overlap[1] >= cur[0]:
                overlap = [cur[0], min(overlap[1], cur[1])]
            else:
                overlap = cur
                cnt += 1

        return cnt
