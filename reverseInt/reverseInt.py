class Solution:
    # @return an integer
    def reverse(self, x):
        absx = int(str(abs(x))[::-1])
        if x >= 0:
            return absx
        else:
            return (-1) * absx
