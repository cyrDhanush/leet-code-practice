class Solution:
    def majorityElement(self, nums):
        majorityElements=[]
        d={}
        for i in nums:
            try:
                count=d[i]
                d[i]=count+1
            except KeyError:
                d[i]=1
        for key,value in d.items():
            if(value>(len(nums)/3)):
                majorityElements.append(key)
        return majorityElements


s=Solution()
print(s.majorityElement([3,2,3]))