  
from collections.abc import Iterable, Iterator
import math


def positive_prices(lines: Iterable[str]) -> Iterator[float]:
    """Takes an iterable of strings and yields a float for each line that is a positive number.
       It skips blank lines, non-numeric lines and non-positive values."""
    
    for line in lines:
        try:
            value = float(line)
        except ValueError:
            continue

        if value > 0 and math.isfinite(value) == True:
            yield value


