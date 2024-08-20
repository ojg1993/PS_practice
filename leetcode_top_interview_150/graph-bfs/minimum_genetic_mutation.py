class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q, visit = deque(), set(startGene)
        q.append((startGene, 0))
        while q:
            cur, cnt = q.popleft()
            if cur == endGene:
                return cnt

            for candidate in bank:
                if candidate not in visit:
                    diff = 0
                    for i in range(len(candidate)):
                        if cur[i] != candidate[i]:
                            diff += 1
                    if diff == 1:
                        q.append((candidate, cnt + 1))
                        visit.add(candidate)
        return -1
