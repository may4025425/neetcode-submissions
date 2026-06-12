class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # 使用集合儲存當前窗口的字符
        left = 0 #左指針
        max_len = 0 #最大長度

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len