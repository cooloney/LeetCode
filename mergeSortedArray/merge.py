"""
Merge Sorted Array
Given two sorted integer arrays A and B, merge B into A as one sorted
array.

Note:
You may assume that A has enough space (size that is greater or equal
to m + n) to hold additional elements from B. The number of elements
initialized in A and B are m and n respectively.
"""

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
	if m <= 0:
		# A.extend(B)
		A.extend([0] * n)
		for i in range(n):
			A[i] = B[i]
		return
	if n <= 0:
		return
        A.extend([0] * n)

	# Merge from the ends of these 2 lists
        p = m + n - 1
       	i = m - 1
	j = m - 1
	while i >= 0:
		x = A[i]
		while j >= 0:
			y = B[j]
			if x > y:
				A[p] = x
				p -= 1
				break
			A[p] = y
			p -= 1 
			j -= 1
		i -= 1

	# Copy the rest elements in B to A
	while p >= 0 and j >= 0:
		A[p] = B[j]
		p -= 1
		j -= 1


if __name__ == "__main__":
	#A = [-10,-10,-9,-9,-9,-8,-8,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-2,-2,-1,-1,0,1,1,1,2,2,2,3,3,3,4,5,5,6,6,6,6,7,7,7,7,8,9,9,9,9]
	#B = [-10,-10,-9,-9,-9,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,9,9,9,9]

	A = [2]
	B = [1]
	s = Solution()
	s.merge(A, len(A), B, len(B))

	print A
