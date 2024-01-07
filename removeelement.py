class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(0, nums.count(val)):
            nums.remove(val)
        return len(nums)
        
s=Solution()
print(s.removeElement([3,2,2,3],3))