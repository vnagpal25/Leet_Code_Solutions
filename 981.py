

class TimeMap:

    def __init__(self):
        # {key: (timestamp, value)}
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]
        # perform binary search to get the value with the largest timestamp less than or equal to timestamp
        l, r = 0, len(values) - 1
        to_ret_t = 0
        to_ret_s = ""

        while l <= r:
            m = (l + r)//2
            
            if values[m][0] > timestamp:
                # definitely not to return, update right pointer
                r = m - 1
            elif values[m][0] < timestamp:
                l = m + 1
                if values[m][0] > to_ret_t:
                    to_ret_t = values[m][0]
                    to_ret_s = values[m][1]
            else:
                return values[m][1]
        
        return to_ret_s


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)