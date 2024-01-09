class Solution:
    upperList=[]
    lowerList=[]
    digitsList=[]
    def __init__(self):
        for i in range(97, 123):
            self.lowerList.append(chr(i))
        for i in range(65, 91):
            self.upperList.append(chr(i))
        for i in range(0, 10):
            self.digitsList.append(i)
        pass

    def checkLowerCase(self, s):
        for i in s:
            if i in self.lowerList:
                return True
        return False
    
    def checkUpperCase(self, s):
        for i in s:
            if i in self.upperList:
                return True
        return False
    
    def checkDigits(self, s):
        for i in s:
            if i in self.digitsList:
                return True
        return False

    def checkRepeatingCharacter(self, s):
        index=0
        lSets=[]
        currentChar=s[0]
        set=0
        while index<len(s)-1:
            if(s[index+1]==currentChar):
                set+=1
            else:
                if(set+1>=3):
                    lSets.append(set+1)
                set=0
                currentChar=s[index+1]
            index+=1
        return lSets
    
    def charCal(self, n):
        pass

    def strongPasswordChecker(self, password: str) -> int:
        #flags
        length=len(password)
        addable=0
        lowerCase=self.checkLowerCase(password)
        upperCase=self.checkUpperCase(password)
        oneDigit=self.checkDigits(password)
        repeatingCharacters=self.checkRepeatingCharacter(password)
        minSteps=0
        if(lowerCase==False):
            minSteps+=1
            addable+=1
        if(upperCase==False):
            minSteps+=1
            addable+=1
        if(oneDigit==False):
            minSteps+=1
            addable+=1
        if(len(repeatingCharacters)==0):
            pass

        pass

s=Solution()
# s.strongPasswordChecker("Baaabb0")
# print(s.checkRepeatingCharacter('aabbbbcbcccb'))