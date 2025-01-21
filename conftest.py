from datetime import datetime, timedelta
from typing import Callable

import pytest


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"\n runtime: {diff.total_seconds()}")


class PerformanceException(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.limit = limit
        self.runtime = runtime

    def __str__(self) -> str:
        return f"Performance test failed runtime: {self.runtime.total_seconds()}, limit: {self.limit.total_seconds()}"

@pytest.fixture
def track_performance():
    def run__function_and_validate_runtime(method: Callable, runtime_limit=timedelta(seconds=2), *args, **kwargs):
        tick = datetime.now()
        result = method(*args, **kwargs)
        tock = datetime.now()
        runtime = tock - tick
        print(f"\n runtime: {runtime.total_seconds()}")

        if runtime > runtime_limit:
            raise PerformanceException(runtime=runtime, limit=runtime_limit)

        return result

    return run__function_and_validate_runtime

