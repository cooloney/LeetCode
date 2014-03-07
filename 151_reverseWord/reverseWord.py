"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        st = ""
        sl = []
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                if start == 1:
                    start = 0
                    sl.append(st)
                    st = ""
                continue
            else:
                start = 1
                st += s[i]
        
        if st != "":
            sl.append(st)
        
	# String splitting doesn't work for input like "   "
        #sl = s.split(" ")
        sl.reverse()
        return " ".join(sl)
