import queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = ""
        q = []
        if root:
            q.append(root)
        while not q:
            t = q.pop(0)
            if t:
                s += "," + str(t.val)
                q.append(t.left)
                q.append(t.right)
            else:
                s += "," + "null"
        return s.lstrip(',')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        tokens = data.split(',')

        if not tokens and tokens[0] != "null":
            return None
        root = TreeNode(tokens.pop(0))
        q = []
        q.append(root)
        while not q:
            t = q.pop(0)
            val = tokens.pop(0)
            if val != "null":
                cur = TreeNode(val)
                q.append(cur)
                t.left = cur

            val = tokens.pop(0)
            if val != "null":
                cur = TreeNode(val)
                q.append(cur)
                t.right = cur

        return root



        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == "__main__":
    print("ttt")