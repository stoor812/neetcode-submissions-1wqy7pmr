class TimeMap:

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []
        self.hash[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""
        elif timestamp < self.hash[key][0][0]:
            return ""
        else:
            # Binary Search 
            lst = self.hash[key]
            left = 0
            right = len(lst) - 1
            max = 0

            while left <= right:
                mid = (left + right) // 2

                if timestamp < lst[mid][0]: # Search Left
                    right = mid - 1
                elif timestamp >= lst[mid][0]: # Search Right
                    max = mid
                    left = mid + 1

            return lst[max][1]

        
