class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        next_node = root
        before_node = None
        first_node = None

        layer_len = 1
        while next_node:
            for i in range(layer_len):
                if next_node is None:
                    continue
                if next_node.left:
                    if before_node:
                        before_node.next = next_node.left
                    before_node = next_node.left
                    if first_node is None:
                        first_node = next_node.left

                if next_node.right:
                    if before_node:
                        before_node.next = next_node.right
                    before_node = next_node.right
                    if first_node is None:
                        first_node = next_node.right

                next_node = next_node.next
            next_node = first_node
            first_node = None
            before_node = None
            layer_len += 1
        return root


if __name__ == '__main__':
    # root = Node(val=1, left=Node(val=2, left=Node(val=4), right=Node(val=5)), right=Node(val=3, right=Node(val=7)))
    root = Node(val=2, left=Node(1), right=Node(3, left=Node(9), right=Node(1)))
    Solution().connect(root)
