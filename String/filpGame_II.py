class Solution(object):
  def canWin(self, s):

    def helper(s, visited):
      # if s in visited:
      #   return visited[s]

      visited[s] = False
      for i in range(0, len(s) - 1):
        if s[i] + s[i + 1] == "++":
          if helper(s[:i] + "--" + s[i + 2:], visited) == False:
            visited[s] = True
      return visited[s]

    visited = {}
    return helper(s, visited)

if __name__ == "__main__":
    cl = Solution()
    s = "++++"
    print(cl.canWin(s))