class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if  s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if not ((s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{')):
                    return False
                stack.pop(-1)
        return len(stack) == 0

if __name__ == "__main__":
    cl = Solution()
    s = '()[]{}'
    print(cl.isValid(s))