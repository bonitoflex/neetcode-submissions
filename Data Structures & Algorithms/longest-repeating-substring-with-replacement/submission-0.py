class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = {}
        ans = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            my_dict[s[r]] = 1 + my_dict.get(s[r], 0)
            maxf = max(maxf, my_dict[s[r]])

            while (r - l + 1) - maxf > k:
                my_dict[s[l]] -= 1
                l += 1

            ans = max(maxf, r - l + 1)

        return ans
