class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if(l<k):
            k=k%l
        n=nums.copy()
        f=n[l-k:]+n[:l-k]
        nums.clear()
        for i in f:
            nums.append(i)
        print(nums)
        
s=Solution()
s.rotate([1,2,3,4,5,6,7],3)
# print(s.rot([1,2,3,4,5,6,7]))