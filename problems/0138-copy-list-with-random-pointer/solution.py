"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      nums, curr, i = [], head, 0
      while curr: 
        nums.append((curr.val, ))
        curr.index = i
        curr = curr.next
        i += 1
      
      i, curr = 0, head
      while curr:
        if curr.random == None: nums[i] += (None, )
        else: nums[i] += (curr.random.index, )
        curr = curr.next
        i += 1

      nodes = [(Node(val), random) for val, random in nums]
      nodes.append((None, None))
      for i in range(0, len(nodes)-1):
        nodes[i][0].next = nodes[i+1][0]
        if nodes[i][1] != None: nodes[i][0].random = nodes[nodes[i][1]][0]
      
      return nodes[0][0]
