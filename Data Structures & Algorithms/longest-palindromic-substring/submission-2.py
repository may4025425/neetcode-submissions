class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(substring):
            return substring == substring[::-1]

        n = len(s)
        max_length = 0
        start = 0 

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and (j-i+1) > max_length:
                    max_length = j-i+1
                    start = i
        
        return s[start:start + max_length]
