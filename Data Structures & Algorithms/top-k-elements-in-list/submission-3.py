class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #bucket sort
        freq = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)
        
        #retrieve k most freq elems
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) >= k:
                    return res
        
        return res