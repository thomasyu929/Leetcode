class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # this solution sort each number in nums
        
        # cur = ""
        # for i in nums:
        #     cur += str(i)
        # return "".join(sorted(cur, reverse = True))
        

        # 1 

        import operator
        import functools
        def cmpFunc(a, b):
            stra, strb = str(a), str(b)
            if stra + strb < strb + stra:
                return -1
            elif stra + strb > strb + stra:
                return 1
            else:
                return 0
        return ''.join(sorted(map(str, nums), key = functools.cmp_to_key(cmpFunc), reverse=True)).lstrip('0') or '0'

        # 2 

        return ''.join(sorted(map(str, nums), key=functools.cmp_to_key(lambda x, y: int(str(x) + str(y)) - int(str(y) + str(x))), reverse = True)).lstrip('0') or "0"