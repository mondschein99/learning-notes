#Question:A phrase is a palindrome if, 
#         after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
#         it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#         Given a string s, return true if it is a palindrome, or false otherwise.

#Original Version
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ''.join(c for c in s if c.isalnum()) #select all aplpha elements in s
        cleaned = cleaned.lower() #make all elements as lower format
        cleaned_reversed = cleaned[::-1] #reverse the string
        return cleaned == cleaned_reversed

#Version to ignore unicode symbols
class Solution(object):
    def isPalindrome(self, s):
        def is_valid(c):
            return unicodedata.category(c)[0] in ('L', 'N')  # Letter or Number

        cleaned = ''.join(c.lower() for c in s if is_valid(c))
        return cleaned == cleaned[::-1]

'''

Note:
unicodedata.category(c) gives things like 'Ll' (lowercase letter), 'Nd' (decimal number), etc.
'L' → all letter types
'N' → numbers

'''
