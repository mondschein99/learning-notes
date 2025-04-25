#Question:Given a string s which consists of lowercase or uppercase letters,
#         return the length of the longest palindrome that can be built with those letters.
#         Letters are case sensitive, for example, "Aa" is not considered a palindrome.


#Original Version
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1
        even_alpha = [k for k, v in counts.items() if v % 2 == 0]
        odd_alpha = [k for k, v in counts.items() if v % 2 == 1] 
        length_max = 0
        for even in even_alpha:
            length_max += counts[even]

        if odd_alpha != []:
            for odd in odd_alpha:
                length_max += counts[odd] - 1
            length_max += 1
        return length_max

#Modified Version
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        length_max = 0
        flag = False
        for count in counts.values():
            if count % 2 == 0:
                length_max += count
            else:
                length_max += count - 1
                flag = True
        if flag:
            length_max += 1

        return length_max

#Selective Version (can build the palindrome)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        length_max = 0
        flag = False
        for count in counts.values():
            if count % 2 == 0:
                length_max += count
            else:
                length_max += count - 1
                flag = True
        if flag:
            length_max += 1

        return length_max

        

