class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        for i, word in enumerate(words):
            if word[0].lower() not in VOWELS: 
                words[i] = word[1:] + word[0]
            words[i] += 'ma' + 'a' * (i+1)
        
        return " ".join(words)
