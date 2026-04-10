class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        arr = []
        length = len(nums)

        # Store all elements in their freq in hashmap
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        buckets = [[] for _ in range(length + 1)]

        for key, val in freq.items():
            buckets[val].append(key)

        for i in range(length, 0, -1):
            for num in buckets[i]:
                if len(arr) == k:
                    return arr
                arr.append(num)

        return arr

