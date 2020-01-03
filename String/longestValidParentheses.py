class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    start = i + 1
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i-start+1)
                    else:
                        res = max(res, i-stack[-1])
        return res
            
            
            
        