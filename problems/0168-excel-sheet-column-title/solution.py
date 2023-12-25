class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''

        while columnNumber > 0:
            if columnNumber <= 26: 
                s = chr(ord('A') -1 + columnNumber % 27) + s
                return s
            else: 
                res = columnNumber % 26
                if res == 0: 
                    res = 26
                    columnNumber -= 26
                s = chr(ord('A') -1 + res) + s
            columnNumber //= 26
        
        return s
