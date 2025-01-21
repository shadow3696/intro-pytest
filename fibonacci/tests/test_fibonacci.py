from typing import Callable
import pytest

from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
from fibonacci.dynamic import fibonacci_dynamic, fibonacci_dynamic_v2
from fibonacci.naive import fibonacci_naive
from fixtures import time_tracker

# @pytest.mark.parametrize(
#     "n,excepted",
#     [
#         (0, 0),
#         (1, 1),
#         (2, 1),
#         (20, 6765),
#     ],
# )
# def test_naive(n: int, excepted: int) -> None:
#     res = fibonacci_naive(n=n)
#     assert res == excepted


@pytest.mark.parametrize("fib_func", [fibonacci_naive, fibonacci_cached, fibonacci_lru_cached, fibonacci_dynamic, fibonacci_dynamic_v2])
@pytest.mark.parametrize(
    "n,excepted",
    [
        (40, 102334155),
    ],
)
def test_cached(time_tracker, fib_func: Callable[[int], int], n: int, excepted: int) -> None:
    res = fib_func(n)
    assert res == excepted
