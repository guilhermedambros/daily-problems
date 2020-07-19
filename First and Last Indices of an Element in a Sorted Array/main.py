# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
class Solution: 
    
  def getRange(self, arr, target):
    ranges = [];
    ranges.append(arr.index(target) if target in arr else -1)#first
    ranges.append(len(arr) - (arr[::-1].index(target) + 1) if target in arr else -1)#last
    return ranges 
    
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8, 11] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

x = 1
print(Solution().getRange(arr, x))
# [0, 0]
x = 10
print(Solution().getRange(arr, x))
# [-1, -1]
x = 11
print(Solution().getRange(arr, x))
# [10, 10]