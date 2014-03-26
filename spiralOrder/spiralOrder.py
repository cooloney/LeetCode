class Solution:
    def _spiral_order(self, sx, sy, ex, ey, matrix, res):
        x = ex - sx + 1
        y = ey - sy + 1
        if x <= 0 or y <= 0:
            return

	# up line
        res.extend(matrix[sy][sx:(ex+1)])
        if y > 1:
	    # right column
            for i in range(sy+1, ey):
                res.append(matrix[i][ex])
	    # bottom line
            res.extend(reversed(matrix[ey][sx:(ex+1)]))
	    if x > 1:
	        # left column
                for i in range(ey-1, sy, -1):
                    res.append(matrix[i][sx])
	        # square
                self._spiral_order(sx+1, sy+1, ex-1, ey-1, matrix, res)

        return

    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        n = len(matrix)
        if n == 0:
            return res
        m = len(matrix[0])

        self._spiral_order(0, 0, m - 1, n - 1, matrix, res)
        return res

if __name__ == "__main__":
    s = Solution()
    m = [
	 [3, 4, 5, 6],
         [7, 8, 9, 2],
         [6, 7, 8, 2],
         [3, 5, 7, 9],
	]
    n = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
    print s.spiralOrder(m)
    print s.spiralOrder(n)

