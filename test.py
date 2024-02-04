import dis

def get(self, key: str, timestamp: int) -> str:
	if key not in self.time_map:
		return ""
	values = self.time_map[key]
	for idx in range(len(values) - 1, -1, -1):
		timestamp_prev, value = values[idx]
		if timestamp_prev <= timestamp:
			return value
	return ""

def get2(self, key: str, timestamp: int) -> str:
	if key not in self.time_map:
		return ""
	values = self.time_map[key]

	def find_upper_bound(values, timestamp):
		left, right = 0, len(values)
		while left < right:
			mid = (left + right) // 2
			timestamp_prev = values[mid][0]
			if timestamp_prev <= timestamp:
				left = mid + 1
			else:
				right = mid
		return left

	upper_bound = find_upper_bound(values, timestamp)
	if upper_bound > 0:
		return values[upper_bound - 1][1]
	return ""

dis.dis(get)
dis.dis(get2)