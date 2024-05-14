class Solution:
    def checksame(self,string):
        j=string[0]
        count=0
        for i in string:
            if i==j:
                count+=1
            else:
                break
        return count
    def romanToInt(self, s: str) -> int:
        # defnum=[1,2,3,10,50,100,500,1000]
        # defsym=['I','V','X','L','C','D','M']
        # num=0
        # for i in s:
        #     while j<len(defsym):
                
        #         j+=1
        # return num
        for i in range(0,len(s)):
            print(self.checksame(s[i:]))
        
a=Solution()
a.romanToInt("LVIII")