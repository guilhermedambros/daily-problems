# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
class Solution: 
    def longestPalindrome(self, s):
      palindromes = []
      s = s+" "
      for i in range(len(s)):
        for j in range(len(s)+1) :
            if Solution().isPalindrome(s[i:j]):
                palindromes.append(s[i:j])
      return Solution().getLongest(palindromes); 
      
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False
        
    def getLongest(self, arr):
        longest = ""
        for item in arr:
            longest = item if len(item) > len(longest) else longest
        
        return longest
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
s = "essa arara é do nahthan hhhhhhhh"
print(str(Solution().longestPalindrome(s)))
#hhhhhhhh