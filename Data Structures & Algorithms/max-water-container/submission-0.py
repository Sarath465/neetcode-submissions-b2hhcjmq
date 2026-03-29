class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1
        while (j>i):
            area = max(area, (j-i)*(min(heights[j], heights[i])))
            if (heights[i] > heights[j]):
                j = j - 1
            else:
                i = i + 1
        return area
        
            
        