class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces, prov_map= [], {}

        for i, row in enumerate(isConnected):
            for j, is_connected in enumerate(row):
                if not is_connected: continue

                if i in prov_map and j in prov_map and prov_map[i] != prov_map[j]:
                    a, b = prov_map[i], prov_map[j]
                    provinces[a].update(provinces[b])
                    for node in provinces[b]: prov_map[node] = a
                    provinces[b].clear()
                    continue
                elif i in prov_map or j in prov_map:
                    ix = prov_map[i] if i in prov_map else prov_map[j]
                else:
                    provinces.append(set())
                    ix = len(provinces) - 1

                provinces[ix].add(i)
                provinces[ix].add(j)
                prov_map[i] = ix
                prov_map[j] = ix
        
        return sum([1 for p in provinces if p])
