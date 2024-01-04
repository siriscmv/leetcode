from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
      counts = defaultdict(int)
      for domain in cpdomains:
        n, d = domain.split(' ')
        n = int(n)

        domains = d.split('.')
        l = len(domains)
        for i in range(0, l): counts[".".join(domains[l-1-i:])] += n
        
      return [" ".join([str(counts[k]), k]) for k in counts]
