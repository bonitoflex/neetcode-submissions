class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        i = 0
        j = len(s1)
        
        freq_s1 = {}
        for ch in s1:
            freq_s1[ch] = freq_s1.get(ch, 0) + 1

        freq_window = {}
        for ch in s2[:j]:
            freq_window[ch] = freq_window.get(ch, 0) + 1

        if freq_s1 == freq_window:
                return True

        while j < len(s2):
            freq_window[s2[i]] -= 1
            if freq_window[s2[i]] == 0:
                freq_window.pop(s2[i])
            freq_window[s2[j]] = freq_window.get(s2[j], 0) + 1
            i += 1
            j += 1
            if freq_s1 == freq_window:
                return True
        return False 