class Solution:
    def merge(self, intervals):
        """
        1. sort intervals
        2. iterate through the intervals
          if res is empty, append the current pair
          if current pair's first value not overlapping the last pair's last value, append current pair
          else update the res's last pair value to have bigger value -> max(res[-1][1], pair[1])
        3. return res
        """
        intervals.sort()
        res = []

        for pair in intervals:
            if not res or res[-1][1] < pair[0]:
                res.append(pair)
            else:
                res[-1][1] = max(res[-1][1], pair[1])
        return res
