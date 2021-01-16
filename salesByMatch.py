#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs_count = 0
    sock_counter = Counter(ar)
    for counter_i in sock_counter:
        pairs_count += sock_counter[counter_i] // 2
    return pairs_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
