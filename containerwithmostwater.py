class Solution:
    def findArea(self, width, height):
        return width*height
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        maxArea=0
        while left<right:
            area=self.findArea(right-left, min(height[left], height[right]))
            maxArea=max(area, maxArea)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxArea
            
        
s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))