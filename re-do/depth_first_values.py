class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# iterative solution
# def depth_first_values(root):
#     if root is None:
#        return [] 
    
#     stack = [ root ]
#     values = []
    
#     while stack:
#         node = stack.pop()

#         # print node val
#         values.append(node.val)

#         # if it has right child
#         if node.right: 
#             stack.append(node.right) 

#         # if it has left child
#         if node.left:
#             stack.append(node.left)

#     return values

# recursive solution
def depth_first_values(root):
    # base case: simplest form of input 
    if root is None:
       return []

    # recursive leap of faith - the subtrees would return a list 
    left_values = depth_first_values(root.left)         # [b, d, e]
    right_values = depth_first_values(root.right)       # [c, f]

    # unpack the array
    return [root.val, *left_values, *right_values]

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(depth_first_values(a))
    #   -> ['a', 'b', 'd', 'e', 'c', 'f']