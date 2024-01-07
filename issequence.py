class Solution(object):
    min=0
    def __init__(self):
        self.min=0
    def findIndex(self, string, chr):
        for i in range(self.min,len(string)):
            if(string[i]==chr):
                return i
        return -1
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        indices=[]
        for i in range(len(s)):
            l=self.findIndex(t, s[i])
            if l==-1:
                return False
            indices.append(l)
            self.min=l
            t=t[:l]+'.'+t[l+1:]
        print(indices)
        if(indices==sorted(indices)):
            return True
        return False
        
        
s=Solution()
print(s.isSubsequence("abca","ahbgdca"))
# print(s.isSubsequence("ab","baab"))
# print(s.findIndex('dhanush', 'a'))