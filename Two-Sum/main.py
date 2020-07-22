# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
def two_sum(list, k):
  for i in range(len(list)):
      for j in range(len(list)):
          if((i != j) and ((list[i] + list[j]) == k)):
              return True
  return False

print (two_sum([4,7,1,-3,2], 5))
# True

print (two_sum([4,7,1,-3,2], 4))
# True

print (two_sum([4,7,1,-3,2], 2))
# False

print (two_sum([4,7,1,-3,2], 10))
# False