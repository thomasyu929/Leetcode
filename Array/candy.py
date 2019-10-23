class Solution:
    def candy(self, ratings: List[int]) -> int:

        '''
        从前往后比较
        从后往前比较
        加和
        两次遍历
        '''


        if not ratings:
            return -1
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
        count = 0 
        for i in candies:
            count += i
        return count

        # 一次遍历，记录后边较小的值，等差数列统计总数

        if not ratings:
            return -1

        pre, count, res = 1, 0, 1
        for i in range(1, len(ratings)):
            if ratings[i-1] <= ratings[i]:
                if count > 0:
                    res += count * (count + 1) // 2
                    if count >= pre:
                        res += count - pre + 1
                    pre = 1
                    count = 0
                if ratings[i-1] == ratings[i]:
                    pre = 1
                else:
                    pre += 1
                res += pre
            else:
                count += 1
        if count > 0:
            res += count * (count + 1) // 2
            if count >= pre:
                res += count - pre + 1
        return res



