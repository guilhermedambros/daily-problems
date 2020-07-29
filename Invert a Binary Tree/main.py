# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#link of online compiler: https://www.programiz.com/python-programming/online-compiler/
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def preorder(self):
        print (self.value),
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()

def invert(root):
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    invert(root.left)
    invert(root.right)

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print ("\n")
invert(root)
root.preorder()
# a c f b e d