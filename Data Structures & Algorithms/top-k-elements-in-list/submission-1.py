class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = k
        ans = []

        # ADD FREQ TO HASHMAP
        for i in nums:     
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        # BUCKETS
        buckets= [[] for _ in range(len(nums) + 1)]
        index = len(buckets) - 1

        for i in freq:
            buckets[freq[i]].append(i)

        while k > 0:
            if len(buckets[index]) == 0:
                index -= 1
            else:
                ans.extend(buckets[index])
                k -= len(buckets[index])
                index -=1

        return ans
