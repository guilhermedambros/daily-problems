# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math
def exists_pythagorean(list):
    for i in range(len(list)):
      for j in range(len(list)):
          if(i != j):
              if math.hypot(list[i], list[j]) in list:
                  return True
    return False

print(exists_pythagorean([3, 5, 12, 5, 13] ))
#True
print(exists_pythagorean([3, 12, 13] ))
#False