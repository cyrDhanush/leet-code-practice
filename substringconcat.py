class Solution:
    def divideString(self, string, n):
        words=[]
        i=0
        while i<(len(string)-(len(string)%n)):
            words.append(string[i:i+n])
            i+=n
        words.sort()
        return words

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        wordListLength=len(words)
        wordLength=len(words[0])
        totalWordsLength=(wordListLength*wordLength)
        sortedWords=sorted(words)
        if(totalWordsLength>len(s)):
            return []
        else:
            indices=[]
            for i in range(0, len(s)-wordListLength+1):
                if(s[i:i+wordLength] in sortedWords):
                    dividedWords = self.divideString(s[i:i+totalWordsLength], wordLength)
                    dividedWords.sort()
                    if(dividedWords==sortedWords):
                        indices.append(i)
                        pass
            return indices
            

s=Solution()
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
print(s.findSubstring("a", ['a']))
# s.divideString("barfoothefoobarman", 3)