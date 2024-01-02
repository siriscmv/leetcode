class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
      items1.sort(key = lambda x: x[0])
      items2.sort(key = lambda x: x[0])

      l1, l2 = len(items1), len(items2)
      ans, i, j = [], 0, 0

      while i<l1 and j<l2:
        a, b = items1[i], items2[j]
        if a[0] < b[0]: 
          ans.append(a)
          i += 1
        elif a[0] > b[0]:
          ans.append(b)
          j += 1
        else:
          ans.append([a[0], a[1]+b[1]])
          i += 1
          j += 1
      
      while i<l1: 
        ans.append(items1[i])
        i += 1
      while j<l2: 
        ans.append(items2[j])
        j += 1

      return ans 
