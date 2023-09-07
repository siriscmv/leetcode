class Solution:
  open = ["(", "{", "["]
  stack = []

  def __init__(self):
    self.stack = []

  def isValid(self, s: str) -> bool:
    if (len(s) == 0): return len(self.stack) == 0
    elif (s[0] in self.open): 
      self.stack.append(s[0])
      return self.isValid(s[1:])
    else: 
      if (len(self.stack) == 0): return False
      
      last = self.stack.pop()
      if (s[0] == ")" and last == "("):  return self.isValid(s[1:])
      elif (s[0] == "}" and last == "{"):  return self.isValid(s[1:])
      elif (s[0] == "]" and last == "["):  return self.isValid(s[1:])
      else: return False
        
