class Solution:
    # recursive solution
    def _numTrees(self, start, end):
        len = end + 1 - start
        if len < 2:
            return 1

        res = 0
        for i in range(start, end + 1):
            res += self._numTrees(start, i - 1) * self._numTrees(i + 1, end)

        return res

    # @return an integer
    def numTrees(self, n):
        return self._numTrees(1, n)
