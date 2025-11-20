from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_abs_diff = sum(abs(num - mean) for num in numbers)
    return total_abs_diff / len(numbers)
