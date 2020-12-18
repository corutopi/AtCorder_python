"""
Common Function
"""

from decorator import stop_watch

# functions
from tool.testcase import random_ints

if __name__ == '__main__':
    for _ in range(1000):
        print(random_ints(2, 1, 10 ** 7, duplicate=False))
