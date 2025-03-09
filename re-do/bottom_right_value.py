from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bottom_right_value(root):
    # queue data structure 
    queue = deque([ (root, 0) ])
    levels_ls = []

    # while the queue is not empty
    while queue:
        # deque pop operation 
        node, level = queue.popleft() # O(1) operation
        levels_ls.append((node.val, level)) # append node.val & level to levels_ls

        # enqueue children onto queue
        if node.left:
            queue.append((node.left, level+1))
            levels_ls.append((node.left.val, level+1))
        if node.right:
            queue.append((node.right, level+1))
            levels_ls.append((node.right.val, level+1))

    # return the sole element of that levels_ls
    if len(levels_ls) < 2:
        return levels_ls[0][0]
    else:
        print(levels_ls)

        # deduce the level ordering from the levels_ls
        last_value, last_level = levels_ls.pop()
        second_last_value, second_last_level = levels_ls.pop()

        if last_level == second_last_level:
            return last_value 
        if second_last_level > last_level:
            return second_last_value 
        else:
            return last_value        

if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(10)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     10
    #  / \      \
    # 4   -2     1

    print(bottom_right_value(a)) # -> 1

    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \       
    #    -2  6

    print(bottom_right_value(a)) # -> 6