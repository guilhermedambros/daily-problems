# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
class Solution:
    
  #secondary function check de match. 
  def match(self, last, current):
    match_list = ["0"]
    if last == "{":
        match_list = ["}"]
    if last == "[":
        match_list = ["]"]
    if last == "(":
        match_list = [")"]
    if current in match_list:
        return True;
    return False;
    
  #secondary function for clear string. 
  #remove characteres out of the list
  def cleanString(self, string):
    list = ["(", "[", "{", ")", "]", "}"]
    new_string = ""
    for c in string:
      if c in list:
        new_string = new_string + str(c);
        
    return new_string;
    
   #main and recursive function
  def isValid(self, string):
    string = Solution().cleanString(string)#clear others chars
    if(len(string) == 0): #when is complete and valid
        return True; 
        
    last = "0"
    new_string = ""
    for c in string:
        if Solution().match(last, c):
            last = "0"
            new_string = new_string[:-1:]#remove the last character that was inserted on the lats lap of the for
        else:
            last = c
            new_string = new_string + str(last)
        
    if string == Solution().cleanString(new_string):#no more checks and not valid
        return False
    else:
       return Solution().isValid(new_string);#new validation
    
  
    
# Test Program
s = "()(){([])}" 
# should return True
print(Solution().isValid(s))

s = "()(){(())" #should return False    
print(Solution().isValid(s)) 

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))