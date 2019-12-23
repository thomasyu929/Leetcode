# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for i in range(len(s)):
#             if  s[i] == '(' or s[i] == '[' or s[i] == '{':
#                 stack.append(s[i])
#             else:
#                 if len(stack) == 0:
#                     return False
#                 if not ((s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{')):
#                     return False
#                 stack.pop(-1)
#         return len(stack) == 0



    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        i = 1
        stack = [s[0]]
        m = {'{':'}', '[':']', '(': ')'}
        if stack[-1] in ['}', ']', ')']:
            return False
        while i <= len(s) - 1:
            if len(stack) != 0 and s[i] == m[stack[-1]]:
                stack.pop()
                i += 1
                continue
            if s[i] in ['{', '[', '(']:
                stack.append(s[i])
                i += 1
            else:
                return False
        return len(stack) == 0

        
if __name__ == "__main__":
    cl = Solution()
    s = '([)]'
    print(cl.isValid(s))