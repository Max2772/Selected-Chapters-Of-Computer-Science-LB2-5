import random


def random_row(N: int):
    """
    Generator of N random float numbers from -10 to 10
    """
    for i in range(N):
        yield round(random.uniform(-10, 10), 4)
