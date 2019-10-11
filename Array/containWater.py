class Solution:
    def maxArea(self, height):

        # # 面积计算以最短边为基准

        # maxarea = 0
        # front = 0
        # rear = len(height) - 1
        # while front < rear:
        #     maxarea = max(maxarea, min(height[front], height[rear]) * (rear-front))
        #     if height[front] < heigth[rear]:
        #         front += 1
        #     else:
        #         rear -= 1
        # return maxarea

        # 每次必会L或R必会向左向右移动一格，所以只需向后遍历

        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
            for w in range(width, 0, -1):
                if height[L] < height[R]:
                    res, L = max(res, height[L] * w), L + 1
                else:
                    res, R = max(res, height[R] * w), R - 1
            return res
