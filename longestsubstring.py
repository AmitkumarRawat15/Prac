def longestsubstring(s):
    left = 0
    maxlength = 0
    ref = set()
    for i in range(len(s)):
        while s[i] in ref:
            ref.remove(s[left])
            left +=1
        ref.add(s[i])
        maxlength = max(maxlength, i - left + 1)
    return maxlength

s = "abcabcbb"
print(longestsubstring(s))