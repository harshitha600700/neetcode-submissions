class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using minheap
        count=Counter(nums)
        return heapq.nlargest(k,count.keys(),key=count.get)
