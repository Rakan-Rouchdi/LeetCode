import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        maxHeap = []
        for stone in stones:
            maxHeap.append(-stone)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone_x = heapq.heappop(maxHeap)
            stone_y = heapq.heappop(maxHeap)
            if stone_x != stone_y:
                heapq.heappush(maxHeap, (stone_x - stone_y))
        
        if not maxHeap:
            return 0
        return -maxHeap[0]

        