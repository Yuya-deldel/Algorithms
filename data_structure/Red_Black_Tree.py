# implementation of Red-Black Tree

RED = 0
BLACK = 1
INF = 1 << 63

class RedBlackNode:
    def __init__(self, data, left=None, right=None, parent=None, color=BLACK):
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data
        self.color = color

class RedBlackTree(RedBlackNode):
    def __init__(self, iterable=[]):
        self.ext = RedBlackNode(None)    # external node = empty black node
        self.ext.left = self.ext
        self.ext.right = self.ext
        self.ext.parent = self.ext
        self.root = self.ext
        self.size = 0
        self.insert_all(iterable)
    
    def count(self, x):
        node = self.find(x)
        d = node.data
        if d == None:
            return False
        else:
            if d != x:
                return False
            else:
                return True
    
    # min{x<=a: a is in RBT}
    def lower_bound(self, x):
        node = self.root
        minimum = INF
        while node != self.ext:
            if x < node.data:
                minimum = node.data
                node = node.left
            elif x > node.data:
                node = node.right
            else:
                return x
        if minimum == INF:
            print("Error: there is no element above " + str(x))
            return INF
        else:
            return minimum

    # max{x>=a: a is in RBT}
    def upper_bound(self, x):
        node = self.root
        maximum = -INF
        while node != self.ext:
            if x < node.data:
                node = node.left
            elif x > node.data:
                maximum = node.data
                node = node.right
            else:
                return x
        if maximum == -INF:
            print("Error: there is no element below " + str(x))
            return -INF
        else:
            return maximum
    
    # insert data:x
    # if this function failed to insert data, return False
    def insert(self, x):
        parent = self.find(x)
        newnode = RedBlackNode(x, left=self.ext, right=self.ext, parent=self.ext, color=RED)
        is_inserted = self.insert_leaf(parent, newnode)    # if insert_leaf function successed to insert newnode, return True
        if is_inserted:
            self.insert_fixup(newnode)
            self.size += 1
        return is_inserted
    
    def insert_all(self, iterable):
        for a in iterable:
            self.insert(a)

    # remove data:x
    # if data:x does not exist, return False
    def erase(self, x):
        lesser_node = self.find(x)
        if (lesser_node != self.ext) and (x == lesser_node.data):
            self.delete(lesser_node)
            self.size -= 1
            return True
        else:
            return False

    ##################################################
    # find node appropriate to insert
    def find(self, x):
        node = self.root
        prev = self.ext
        while node != self.ext:
            prev = node
            if x < node.data:
                node = node.left
            elif x > node.data:
                node = node.right
            else:
                return node
        return prev
    
    # insert leaf-node
    def insert_leaf(self, parent, child):
        if parent == self.ext:
            self.root = child
        else:
            child.parent = parent
            if child.data < parent.data:
                parent.left = child
            elif child.data > parent.data:
                parent.right = child
            else:
                return False
        return True
    
    def insert_fixup(self, node):
        while node.color == RED:
            parent = node.parent
            if node == self.root:
                node.color = BLACK
                return
            if parent.left.color == BLACK:
                self.flip_left(parent)
                node = parent
                parent = node.parent
            if parent.color == BLACK:
                return
            grandparent = parent.parent
            if grandparent.right.color == BLACK:
                self.flip_right(grandparent)
                return
            self.push_black(grandparent)
            node = grandparent
    
    # when node has 2 child, find minimum-value node(alt) and substitute
    #     node            alt
    #    /    \          /   \
    #   A      B    =>  A     B
    #         / \              \
    #       alt  C              C
    def delete(self, node):
        if node.left == self.ext or node.right == self.ext:
            self.splice(node)
        else:
            altnode = node.right
            while altnode.left != self.ext:
                altnode = altnode.left
            node.data = altnode.data
            self.splice(altnode)
        
    def splice(self, node):
        if node.left != self.ext:
            leaf = node.left
        else:
            leaf = node.right

        if node == self.root:
            self.root = leaf
            parent = self.ext
        else:
            parent = node.parent
            if parent.left == node:
                parent.left = leaf
            elif parent.right == node:
                parent.right = leaf

        leaf.parent = parent        
        leaf.color += node.color
        self.remove_fixup(leaf)

    def remove_fixup(self, node):
        while node.color > BLACK:
            if node == self.root:
                node.color = BLACK
            elif node.parent.left.color == RED:
                self.flip_right(node.parent)
                node = self.remove_fixup_case2(node)
            elif node == node.parent.left:
                node = self.remove_fixup_case1(node)
            else:
                node = self.remove_fixup_case2(node)
        
        if node != self.root:
            parent = node.parent
            if parent.right.color == RED and node.color == BLACK:
                self.flip_left(parent)
    
    def remove_fixup_case1(self, node):
        w = node.parent
        v = w.right
        self.pull_black(w)
        self.flip_left(w)
        q = w.right
        if q.color == RED:
            self.flip_left(w)
            self.flip_right(v)
            self.push_black(q)
            if v.right.color == RED:
                self.flip_left(v)
            return q
        else:
            return v
    
    def remove_fixup_case2(self, node):
        w = node.parent
        v = w.left
        self.pull_black(w)
        self.flip_right(w)
        q = w.left
        if q.color == RED:
            self.flip_right(w)
            self.flip_left(v)
            self.push_black(q)
            return q
        elif v.left.color == RED:
            self.push_black(v)
            return v
        else:
            self.flip_left(v)
            return w

    # subroutines
    #
    #           pull
    #     B     <===      R
    #    / \    ===>     / \
    #   R   R   push    B   B

    def push_black(self, node):
        node.color -= 1
        node.left.color += 1
        node.right.color += 1
    
    def pull_black(self, node):
        node.color += 1
        node.left.color -= 1
        node.right.color -= 1
    
    # transformation which keep Heap property
    #         w                u 
    #        / \     rotR     / \
    #       u   C    ===>    A   w
    #      / \       <===       / \
    #     A   B      rotL      B   C

    def rotate_left(self, u):
        # w --- u's parent
        w = u.right
        w.parent = u.parent
        if w.parent != self.ext:
            if w.parent.left == u:
                w.parent.left = w
            elif w.parent.right == u:
                w.parent.right = w
        else:
            self.root = w
        # u --- B
        u.right = w.left
        if u.right != self.ext:
            u.right.parent = u
        # u --- w
        u.parent = w
        w.left = u

    def rotate_right(self, w):
        # u --- w's parent
        u = w.left
        u.parent = w.parent
        if u.parent != self.ext:
            if u.parent.left == w:
                u.parent.left = u
            elif u.parent.right == w:
                u.parent.right = u
        else:
            self.root = u
        # w --- B
        w.left = u.right
        if w.left != self.ext:
            w.left.parent = w
        # u --- w
        w.parent = u
        u.right = w
    
    # rotate + color change
    #         B                 B 
    #        / \     flipR     / \
    #       R   B    ===>     B   R
    #      / \       <===        / \
    #     B   B      flipL      B   B

    def flip_left(self, u):
        w = u.right
        (u.color, w.color) = (w.color, u.color)
        self.rotate_left(u)
    
    def flip_right(self, w):
        u = w.left
        (w.color, u.color) = (u.color, w.color)
        self.rotate_right(w)


    # imprementation of iterator
    def __iter__(self):
        node = self.first_node()
        while node != self.ext:
            yield node.data
            node = self.next_node(node)
    
    def first_node(self):
        node = self.root
        if node == self.ext:
            return self.ext
        while node.left != self.ext:
            node = node.left
        return node
    
    def next_node(self, node):
        if node.right != self.ext:
            node = node.right
            while node.left != self.ext:
                node = node.left
        else:
            while (node.parent != self.ext) and (node.parent.left != node):
                node = node.parent
            node = node.parent
        return node