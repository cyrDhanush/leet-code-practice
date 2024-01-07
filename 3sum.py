class Solution:
    # def removeDuplicates(self, l):
    #     l.sort()
    #     uniqueList=[]
    #     for i in l:
    #         if i not in uniqueList:
    #             uniqueList.append(i)
    #     return uniqueList
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums=self.removeDuplicates(nums.copy())
        s=[]
        for i in range(len(nums)):
            for j in range(i):
                for k in range(j):
                    if(nums[i]+nums[k]+nums[j]==0):
                        res=[nums[i],nums[j],nums[k]]
                        res=sorted(res)
                        if(res not in s):
                            s.append(res)
        return s
        

s=Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))