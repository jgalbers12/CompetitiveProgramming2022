"""
file: longest_increasing_subsequence.py
author: @jalbers
"""

from sys import stdin,stdout

while(True):
    try:
        n  = int(stdin.readline())
    except:
        break
    nums = [int(x) for x in stdin.readline().split()]
    maxi = [-1] * (n + 1)# stores last index of longest subsequence of length i
    prev = [-1] * n # stores previous index of longest subsequence ending in i
    length = 0 # length of longeset subsequence

    for i in range(0, len(nums)):
        # binary search on maxi
        low = 1
        high = length + 1
        while low < high:
            mid = (low + high) // 2
            if nums[maxi[mid]] > nums[i]:
                high = mid
            elif nums[maxi[mid]] < nums[i]:
                low = mid + 1
            else:
                low = mid
                break
        #print(f"num: {nums[i]} low: {low}")
        if low > length:
            length = low
        prev[i] = maxi[low-1]
        maxi[low] = i

    sequence = [None] * length
    index = maxi[length]

    for j in range(length-1, -1, -1):
        sequence[j] = index
        index = prev[index]
    stdout.write(str(length)+"\n")
    for i in range(len(sequence) - 1):
        stdout.write(f"{sequence[i]} ")
    stdout.write(str(sequence[-1])+"\n")
