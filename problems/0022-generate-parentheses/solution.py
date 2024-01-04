class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      ans = set()
      for i in range(1, n+1):
        stack = ['('] * i
        while stack:
          top = stack.pop()
          if top.count('(') < n: stack.append(top + '(')
          if top.count('(') > top.count(')') : stack.append(top + ')')
          if top.count('(') == top.count(')') == n: ans.add(top)
      return list(ans)
