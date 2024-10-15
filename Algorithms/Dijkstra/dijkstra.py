from collections import defaultdict
import heapq
from typing import List, Dict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = defaultdict(list)

        for source, dest, weight in edges:
            adjList[source].append((weight, dest))
        
        print(adjList)
        
        minHeap = [[0, src]]
        res = {}
        while minHeap:
            weight, source = heapq.heappop(minHeap)

            if source in res:
                continue
            
            res[source] = weight

            for nextWeight, destination in adjList[source]:
                if destination not in res:
                    heapq.heappush(minHeap, [weight + nextWeight, destination])

        for idx in range(n):
            if idx not in res:
                res[idx] = -1

        return res
