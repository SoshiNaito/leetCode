#!/bin/python3

import math
import os
import random
import re
import sys

TWO_STEP_COUNT = 2
AJUST_INDEX = 1
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump_count = 0
    current_index = 0
    while current_index < len(c) - TWO_STEP_COUNT:
        if c[current_index + TWO_STEP_COUNT] == 1:
            current_index += 1
        else:
            current_index += 2
        jump_count += 1

    if current_index == len(c) - TWO_STEP_COUNT:
        jump_count += 1
    return jump_count


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
    # fptr.write(str(result) + "\n")

    # fptr.close()
