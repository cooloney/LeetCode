class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) == 0 or len(T) == 0:
            return ""

        queue = []
        hashT = {c : 0 for c in T}
        foundT = {c : 0 for c in T}

        for c in T:
            hashT[c] += 1

        start = found = 0
        minLen = len(S)
        res = ""

        # Move end pointer i
        for i in range(len(S)):
            c = S[i]
            if c in T:
                queue.append(i)
                foundT[c] += 1
                if foundT[c] <= hashT[c]:
                    found += 1
                # Found a substring has T
                if found == len(T):
                    # move start point
                    while start <= i:
                        start = queue[0]
                        # continue move start point
                        if foundT[S[start]] - 1 >= hashT[S[start]]:
                            queue.pop(0)
                            foundT[S[start]] -= 1
			    continue

                        # Found current minimun window
                        # Update result
                        if i - start + 1 <= minLen:
                            minLen = i - start + 1
                            res = S[start:i+1]
                        queue.pop(0)
                        foundT[S[start]] -= 1
			found -= 1
                        break
        return res

if __name__ == "__main__":
    s = Solution()
    S = "cabefgecdaecf"
    T = "cae"

    print S, T
    print s.minWindow(S, T)
