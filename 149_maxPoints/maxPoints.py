'''
Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

'''
Analyze:
Calculating slope of a line is the key point of the solution
1. For each point of the list, calculate the slope of lines start from the point
2. store the slopes and count the number
3. save the max number points of the line starting from the point
4. get the max number points after looping

NOTE: don't use any built-in sorting method which will cause timeout
'''

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    # for print usage
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
	num_points = len(points)
	# 2 points make a line
        if num_points <= 2:
            return num_points

        # max_points for each point in the list
        max_points = 0
        for i in range(num_points):
	    # a dict to store slopes and numbers of those lines having the same slope
            slopes = {}
	    # duplicated pionts
            nums_same_point = 0
	    # number of max points in one line started from point[i]
            tmp_max_points = 0
	    # vertical line
	    infinity_slopes = 0
            for j in range(i+1, num_points):
                p = points[i]
                q = points[j]
	        # duplicated pionts
                if p.x == q.x and p.y == q.y:
                    nums_same_point += 1
	        # vertical line
		elif p.x == q.x and p.y != q.y:
                    if infinity_slopes > 0:
                        infinity_slopes += 1
                    else:
                        infinity_slopes = 2
                    if tmp_max_points < infinity_slopes:
                        tmp_max_points = infinity_slopes
	        # normal lines
                else:
		    # don't use abs(), slope can be less than 0
                    s = float(p.y - q.y) / (p.x - q.x)
                    if s in slopes.keys():
                        slopes[s] += 1
                    else:
                        slopes[s] = 2
                    if tmp_max_points < slopes[s]:
                        tmp_max_points = slopes[s]
	    # normal case
	    if tmp_max_points > 0:
	        tmp_max_points = nums_same_point + tmp_max_points
	    # special case, every points of the input list are the same, see testcase 2
	    else:
		tmp_max_points = nums_same_point + 1

            if max_points < tmp_max_points:
                max_points = tmp_max_points

        return max_points

# Test case for debugging
def main():
    # Test case 1
    points = [(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)]
    # Test case 2
    points = [(0,-12),(5,2),(2,5),(0,-5),(1,5),(2,-2),(5,-4),(3,4),(-2,4),(-1,4),(0,-5),(0,-8),(-2,-1),(0,-11),(0,-9)]
    # Test case 3
    points = [(1,1),(1,1),(1,1)]
    pts = [Point(points[k][0], points[k][1]) for k in range(len(points))]
    print pts
    s = Solution()
    print s.maxPoints(pts)

if __name__ == "__main__":
    main()
