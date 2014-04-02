class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        
        m = len(grid[0])
        n = len(grid)
        
        # d = [[0] * m] * n, THIS IS WRONG
        d = [[0] * m for i in range(n)]
        
        d[0][0] = grid[0][0];
	print "d[0][0]"
	print d
        for i in range(1, m):
            d[0][i] = d[0][i-1] + grid[0][i]
	print "d[0][i]"
	print d
        
        for i in range(1, n):
            d[i][0] = d[i-1][0] + grid[i][0]
	print "d[i][0]"
	print d
        
        for i in range(1, m):
            for j in range(1, n):
                d[j][i] = min(d[j-1][i], d[j][i-1]) + grid[j][i]
    
        print
	print d    
        return d[n-1][m-1]

if __name__ == "__main__":
    g = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]
    print g
    s = Solution()
    print s.minPathSum(g)
