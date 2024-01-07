class Solution(object):
    alpha=[]
    def __init__(self):
        self.alpha=[]
        for i in range(97,123):
            self.alpha.append(chr(i))
        for i in range(0,10):
            self.alpha.append(str(i))
    def cleanIt(self, string):
        cstring=string
        for i in string:
            if i not in self.alpha:
                cstring=cstring.replace(i,'')
        return cstring
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=self.cleanIt(s)
        if(s==s[::-1]):
            return True
        else:
            return False


s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))