"""
file: biased_standing.py
author: @jalbers
"""

from sys import stdin, stdout

total, min_dist, num_birds = [int(x) for x in stdin.readline().split()]

positions = [-1] * num_birds

for i in range(num_birds):
    positions[i] = int(stdin.readline())

positions.sort()

extra = 0

if len(positions):
    beginning_segments = (positions[0] - 6) // min_dist
    if beginning_segments > 0:
        extra += beginning_segments
    end_segments = ((total - 6) - positions[-1]) // min_dist
    if end_segments > 0:
        extra += end_segments
else:
    segments = ((total - 6) - 6) // min_dist
    if segments >= 0:
        extra += segments + 1

for j in range(num_birds-1):
    min_segments = (positions[j+1] - positions[j]) // min_dist
    if min_segments > 0:
        extra += min_segments - 1

# last_birds = ((total - 6) - start) // min_dist
# if last_birds > 0:
#     extra += last_birds - 1

stdout.write(str(extra))
