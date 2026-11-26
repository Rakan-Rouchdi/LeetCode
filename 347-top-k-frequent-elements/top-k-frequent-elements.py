import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {} # key -> number : value -> count
        minHeap = []
        frequent = []
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        for number, count in count.items():
            heapq.heappush(minHeap, (count, number))
        
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        while minHeap:
            temp = heapq.heappop(minHeap)
            frequent.append(temp[1])
        
        return frequent

        
        

        

        