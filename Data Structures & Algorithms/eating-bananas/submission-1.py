
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1#minimum possible speed=1
        r=max(piles)#maximum possible speed =largest pile (eat in one hour)
        res=r   #(stores the best valid answer)
        while l<=r:
            m=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/m)#ceiling for rounding off
            if hours<=h:
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res

        