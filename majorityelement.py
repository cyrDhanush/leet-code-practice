class Solution:
    def majorityElement(self, nums):
        d={}
        for i in nums:
            try:
                count=d[i]
                d[i]=count+1
            except KeyError:
                d[i]=1
        for key,value in d.items():
            if(value>(len(nums)/2)):
                return key


s=Solution()
print(s.majorityElement([3,2,3]))