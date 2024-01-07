class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=2):
            return len(nums)
        i=2
        for i in nums:
            s=nums.count(i)
            if(s>=3):
                for k in range(s-2):
                    nums.remove(s)
        return nums
        

        
        
s=Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))
# print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))