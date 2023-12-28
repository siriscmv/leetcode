class Solution:
    def getForm(self, s: str):
        form, seen = [], {}
        i, l = 0, len(s)
        while i < l:
            j = i+1
            while j < l and  s[j] == s[i]: j += 1
            char = s[i]
            if char in seen: form.append((j-i, seen[char])) 
            else:
                seen[char] = len(form)
                form.append((j-i, None))
            i = j
        return form

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return all(a == b for a, b in zip(self.getForm(s), self.getForm(t)))
