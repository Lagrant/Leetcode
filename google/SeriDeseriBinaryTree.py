# Definition for a binary tree node.
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
        if (root is None):
            return ''
        nodes = [root]
        seri = str(root.val) + '|'
        idx = 0
        while (idx < len(nodes)):
            # cur = nodes.popleft()
            
            if (nodes[idx].left):
                nodes.append(nodes[idx].left)
                seri += str(nodes[idx].left.val) + '*' + str(idx) + '*0' + '|'

            if (nodes[idx].right):
                nodes.append(nodes[idx].right)
                seri += str(nodes[idx].right.val) + '*' + str(idx) + '*1' + '|'

            idx += 1
        return seri

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if (len(data) == 0):
            return None
        
        seri_nodes = data.split('|')[:-1]

        root = TreeNode(int(seri_nodes[0]))
        nodes = [root]

        for i in range(1, len(seri_nodes)):
            seri = seri_nodes[i].split('*')
            cur = TreeNode(int(seri[0]))
            parent = int(seri[1])
            side = int(seri[2])

            if (side == 0):
                nodes[parent].left = cur
            else:
                nodes[parent].right = cur
            
            nodes.append(cur)

        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
rright = root.right
rright.left = TreeNode(4)
rright.right = TreeNode(5)

code = Codec()
data = code.serialize(root)
# print(data)
code.deserialize(data)