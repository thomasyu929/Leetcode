class Solution:
    
    # 1

    def isSubsequence(self, s: str, t: str) -> bool:

        import collections
        import bisect

        # bisect() just return the index of value, not insert value into array
        # and insort() insert the value to array, no return

        start = 0

        m = collections.defaultdict(list)
        for i, c in enumerate(t):
            m[c].append(i)
        for c in s:
            idx = bisect.bisect_left(m[c], start)
            if len(m[c]) == 0 or idx >= len(m[c]):
                return False
            start = m[c][idx] + 1
        return True

    # 2

    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)

    # 3 same as 2    but explain 2
    def isSubsequence(self, s, t):
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True


if __name__ == "__main__":
    cl = Solution()
    s = "abc"
    t = "ahagabbgdc"
    print(cl.isSubsequence(s, t))