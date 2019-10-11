class Solution:
    def trap(self, height: List[int]) -> int:
        
        '''
        将其看作为一个整体
        计算所有黑块的值以及以最高点为限的空白处的值
        总体减去即为雨水值
        
        '''
        if not height:
            return 0
        blockArea, upArea, highest = 0, 0, 0
        node = -1
        for i in range(len(height)):
            blockArea += height[i]
            if height[i] > highest:
                highest = height[i]
                node = i
        
        h = 0
        for i in range(node):
            h = max(h, height[i])
            upArea += highest - h
        h = 0
        for i in range(len(height)-1, node, -1):
            h = max(h, height[i])
            upArea += highest - h
        return (len(height) * highest) - upArea - blockArea