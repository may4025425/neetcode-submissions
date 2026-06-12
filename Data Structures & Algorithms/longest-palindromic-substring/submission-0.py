class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(substring):
            # 判斷是否是回文
            return substring == substring[::-1]

        n = len(s)
        max_length = 0
        start = 0  # 記錄最長回文子串的起始位置

        # 枚舉所有子串
        for i in range(n):
            for j in range(i, n):
                # 獲取子串
                substring = s[i:j+1]
                # 判斷是否是回文，且長度是否更長
                if is_palindrome(substring) and (j - i + 1) > max_length:
                    max_length = j - i + 1
                    start = i

        # 返回最長回文子串
        return s[start:start + max_length]
