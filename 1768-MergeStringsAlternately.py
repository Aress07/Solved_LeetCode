class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        l = min(len(w1), len(w2))
        i = 0
        j = 0
        S = ""
        for n in range(l):
            S += "".join(w1[i])
            S += "".join(w2[j])         
            i += 1
            j += 1
        
        if len(w1) < len(w2):
            S += word2[j:]
        if len(w1) > len(w2): 
            S += word1[i:]
        return S
