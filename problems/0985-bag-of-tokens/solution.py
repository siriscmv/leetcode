class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        ans, score = 0, 0
        l, r = 0, len(tokens) - 1
        
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                ans = max(ans, score)
            elif score > 0:           
                power += tokens[r]
                score -= 1
                r -= 1
            else: break

        return ans
