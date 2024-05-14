class Solution:
    def kthFactor(self, n, k):
        factCount=1
        num=n
        i=1
        while True:
            if(i>num):
                return -1
            if(num%i==0):
                if(factCount==k):
                    return i
                else:
                    factCount+=1
            i+=1
        

s=Solution()
print(s.kthFactor(12,3))
print(s.kthFactor(7,2))
print(s.kthFactor(4,4))