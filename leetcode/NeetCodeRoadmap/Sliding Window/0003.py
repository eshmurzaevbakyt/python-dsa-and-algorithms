def lengthOfLongestSubstring(self, s):
    charSet = set()
    l, res = 0, 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[r])
            l += 1
        charSet.add(s[r])
        res = max(res, l - r + 1)
    return res
