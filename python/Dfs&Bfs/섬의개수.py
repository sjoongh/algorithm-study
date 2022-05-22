from collections import deque
import sys

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    