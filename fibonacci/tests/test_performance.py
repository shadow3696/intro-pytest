import pytest
from fibonacci.dynamic import fibonacci_dynamic_v2
from conftest import track_performance
from typing import Callable
from datetime import timedelta

@pytest.mark.performance
@pytest.mark.parametrize("fib_func", [fibonacci_dynamic_v2])
@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (10, 55),
        (20, 6765),
        (30, 832040),
        (40, 102334155),
        (50, 12586269025),
        (60, 1548008755920),
        (1000, 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875),
    ],
)
def test_performance(track_performance, fib_func: Callable[[int], int], n: int, expected: int):
    result = track_performance(fib_func, runtime_limit=timedelta(seconds=2), n=n)
    assert result == expected
