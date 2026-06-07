class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        bucket sort
        '''

        # Map freq of nums in our dictionary 
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Bucket sort
        # create a list of lists
        freq = [[] for i in range(len(nums)+1)]
        # Extract the number and the count from our dictionary to put into buckets
        for n, c in count.items():
            freq[c].append(n)
        
        #Go through our frequency array in reverse order
        #Extract the numbers from most occurring to least and append to our results array
        #which we return
        res = []

        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res


        

