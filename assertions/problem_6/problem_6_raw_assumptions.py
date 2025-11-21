# res is the mean absolute deviation around the mean of `numbers`

# 1. Result is always non-negative
assert res >= 0

# 2. If numbers is empty, MAD must be 0
assert (len(numbers) == 0) == (res == 0)

# 3. If all values in numbers are identical, MAD is 0
assert (all(x == numbers[0] for x in numbers) if numbers else True) == (res == 0)

# 4. Let μ be the arithmetic mean; res equals the average absolute deviation
mean = (sum(numbers) / len(numbers)) if numbers else 0
assert res == (sum(abs(x - mean) for x in numbers) / len(numbers)) if numbers else (res == 0)

# 5. MAD is invariant under adding a constant to all elements
k = 5.0  # any constant shift; pure logic, no side effects
shifted = [x + k for x in numbers]
mean_shifted = (sum(shifted) / len(shifted)) if numbers else 0
mad_shifted = (sum(abs((x + k) - mean_shifted) for x in numbers) / len(numbers)) if numbers else 0
assert (res == mad_shifted) if numbers else (res == 0)
