from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []

        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            ix = bisect_left(products, prefix)
            ans.append([s for s in products[ix:ix+3] if s.startswith(prefix)])

        return ans
