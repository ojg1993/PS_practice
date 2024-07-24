class Solution:
    def insert(self, intervals, newInterval):
        """
        1. intervals are not overlapping
        2. intervals are sorted
        3. insert newInterval into intervals
          case
            a. newInterval is not overlapping and less the current interval
              -> append newInterval and update newInterval to current interval(very important)
            b. newInterval is not overlapping and bigger than the current interval
              -> append(interval)
            c. newInterval is overlapping the current interval
              -> update newInterval to [min, max]
        4. append newInterval there's always one interval not appended(very important)
        5. return res
        Int:    ---    --- --- ---
        New: --     --   ------    ---
        """

        res = []
        for interval in intervals:
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        res.append(newInterval)
        return res
