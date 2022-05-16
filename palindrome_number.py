class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 & (x % 10 == 0 & x != 0):
            return False
        reversed_number = 0
        while x > reversed_number:
            if x // 10 == reversed_number:
                return True
            reversed_number = reversed_number * 10 + (x % 10)
            x = x // 10
        return x == reversed_number:
