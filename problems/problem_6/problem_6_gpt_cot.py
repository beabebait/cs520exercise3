from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate Mean Absolute Deviation around the mean.
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0
    mean_value = sum(numbers[:-1]) / len(numbers)
    absolute_deviations = [abs(x - mean_value) for x in numbers]
    mad = sum(absolute_deviations) / len(numbers)
    return mad
