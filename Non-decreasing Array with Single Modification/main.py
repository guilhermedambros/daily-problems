# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
def check(list):
  count_diff = 0
  for i in range(len(list)-1):
      if list[i+1] > list[i]:
          count_diff += 1
      
  return (count_diff <=1)


print (check([13, 4, 7]))
# True
print (check([5,1,3,2,5]))
# False