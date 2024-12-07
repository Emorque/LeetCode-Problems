from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        low, high = 0, len(self.store[key]) - 1
        while low <= high:
            mid = low + (high - low) // 2
            ts, val = self.store[key][mid]
            if ts == timestamp:
                return val
            elif ts < timestamp:
                value = val
                low = mid + 1
            else:
                high = mid - 1
        return value   


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)