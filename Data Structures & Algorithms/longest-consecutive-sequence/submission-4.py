class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)#removes duplicates
        longest=0#stores max sequence length

        for n in nums:
            if (n-1) not in numSet:#check if start of sequence
                length=1
                while (n+length) in numSet:
                    length+=1
                longest=max(longest,length)
        return longest
