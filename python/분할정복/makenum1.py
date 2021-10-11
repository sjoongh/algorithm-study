import sys

X = int(sys.stdin.readline())

while X > 0:
    if X // 3 == 0:
       X = X // 3
    elif X // 2 == X % 2 == 0:
        X = X // 2
    else:
        X -= 1
    
