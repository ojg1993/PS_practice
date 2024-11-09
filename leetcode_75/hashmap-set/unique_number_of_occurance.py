class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = defaultdict(int)

        for num in arr:
            hash_map[num] += 1
        return len(hash_map.values()) == len(set(hash_map.values()))
