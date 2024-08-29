1. Share questions you would ask to help understand the question:
- Will there be a key in get that is not in the timemap?
- Are the set values always in ascending order?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Binary Search (Likely)
- Hashmap (Likely)

3. Write out in plain English what you want to do: 
- From the class description, using a hashmap appears to be the first step, where the key is the string like "foo", and the value are any added set lists from the set command
- Then, for set, that list just gets added to the list of the matching key in the hashmap 
- As for get, since the timestamps from set are in ascending order, than binary serach instead of a linear search can be used 
  - Perform binary search on the list of the matching key. 

4. Translate each sub-problem into pseudocode:
  - __init__:
    - set this to a hash map where the key the string (ex: "foo"), and the value is a list of lists (ex: ["bar", 1], ["bar", 3])

  - set: 
    - if the key is not in the hashmap: 
      - initialize it to the hashmap with a blank list 
    - append the list (ex: ["bar", 3])) to the list 

  - get
    - get the list from the matching key in the hashmap 
    - set low, high to 0, len(list)
    - while low <= high:
      - mid = low + (high - low) // 2
      - output = ""
      - if list[mid][1] == timestamp:
        - return list[mid][0]
      - elif list[mid][1] < timestamp: 
        - output = list[mid][0]
        - low = mid + 1
      - else:
        - high = mid - 1
    - if nothing is returned, return output which should have the next highest timestamp 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class TimeMap:

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
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that since binary search is used in the get function, the time complexity is O(log(n)) instead of O(n) for a linear search 
- One weak area is that it could be faster with using defaultdict() for the hashmap intitialization, and using the get method for retriving the list in the get function. 