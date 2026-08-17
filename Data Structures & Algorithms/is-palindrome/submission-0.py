class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for x in s:
            if x.isalnum():
                a += x.lower()
        return a == a[::-1]