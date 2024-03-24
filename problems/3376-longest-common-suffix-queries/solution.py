class Node:
    def __init__(self, value):
        self.value = value
        self.next = []
        self.mp = {}     

    def add_next(self, char):
        if char in self.mp: return self.mp[char]
        
        self.next.append(Node(char))
        self.mp[char] = len(self.next) -1
        return self.mp[char]
    
    def is_end(self):
        return 0 in self.mp
        
    def add_word(self, word):
        if not word: 
            self.mp[0]=0
            return
        
        ix = self.add_next(word.pop())
        self.next[ix].add_word(word)
    
    def get_word(self, word, curr, take_first):
        if self.is_end() and (take_first or not(word) or len(self.next) == 0 or word[-1] not in self.mp): return curr
        if not word: take_first = True
        
        if take_first: ix = 0
        else: 
            if word[-1] in self.mp: ix = self.mp[word[-1]]
            else:
                ix = 0
                take_first = True
        
        curr.appendleft(self.next[ix].value)
        if word: word.pop()
        return self.next[ix].get_word(word, curr, take_first)        

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        mp = {}
        graph, ans = Node(-1), []
        
        for i, word in enumerate(wordsContainer): 
            if word not in mp: mp[word] = i
        words = sorted(enumerate(wordsContainer), key=lambda x: (len(x[1]), mp[x[1]]))
        for word in words: graph.add_word(list(word[1]))
        
        for q in wordsQuery:
            w = graph.get_word(list(q), deque(), False)
            w = "".join(w)
            ans.append(mp[w])
            
        return ans
