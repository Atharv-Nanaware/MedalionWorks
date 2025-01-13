import csv
import os
import random
from datetime import datetime, timedelta
from typing import Generator
from faker import Faker

fake = Faker()


def id_generator(start: int = 1) -> Generator[int, None, None]:
    """
    Returns an incremental ID generator starting from `start`.

    Yields:
        int: The next ID in sequence.
    """
    current = start
    while True:
        yield current
        current += 1
