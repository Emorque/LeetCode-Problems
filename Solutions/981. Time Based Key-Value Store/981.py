class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap: 
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        output = ""
        if key not in self.hashmap: 
            return output
        valList = self.hashmap[key]
        low, high = 0, len(valList) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if valList[mid][1] == timestamp:
                return valList[mid][0]
            elif valList[mid][1] < timestamp:
                output = valList[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return output