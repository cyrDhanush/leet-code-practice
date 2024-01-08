class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                print(i,j)
        pass
        
s=Solution()
s.minCapability([2,3,5,9])