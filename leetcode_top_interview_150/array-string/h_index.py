class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        hidx = 0

        for i in range(len(citations)):
            if i + 1 <= citations[i]:
                hidx = i + 1
            else:
                break

        return hidx
