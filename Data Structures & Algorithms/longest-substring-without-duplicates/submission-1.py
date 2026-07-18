class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        my_dict = {}
        r = 0
        l = 0
        maxi = 0
        
        while r < n:
            if s[r] in my_dict:
                l = max(l, my_dict[s[r]] + 1)
            maxi = max(maxi, r-l+1)
            my_dict[s[r]] = r
            r += 1
        return maxi
            