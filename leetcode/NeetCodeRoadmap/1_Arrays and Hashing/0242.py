import collections
from collections import Counter
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    CountS, CountT = {}, {}
    for i in range(len(s)):
        CountS[s[i]] = 1 + CountS.get(s[i], 0)
        CountT[t[i]] = 1 + CountT.get(t[i], 0)
    for c in CountS:
        if CountS[c] != CountT.get(c, 0):
            return False
    return True
#Other solutions
def isAnagram2(self, s, t):
    return Counter(s) == Counter(t)

def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)

