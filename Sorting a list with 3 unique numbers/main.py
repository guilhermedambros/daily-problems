# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
class Solution:
    
  def sortNums(self, nums):
    nums.sort()
    return nums

nums=[3, 3, 2, 1, 3, 2, 1]
print(Solution().sortNums(nums))
# [1, 1, 2, 2, 3, 3, 3]