# Q1. Course Registration
T = int(input())
for i in range(T):
    N, M, K = list(map(int, input().split()))
    if N <= (M-K):
        print("Yes")
    else:
        print("No")

# Q2. Battery Low
T = int(input())
for i in range(T):
    X = int(input())
    if X <= 15:
        print("Yes")
    else:
        print("No")

# Q3. Bucket and Water Flow
T = int(input())
for i in range(T):
    W, X, Y, Z = list(map(int, input().split()))
    total_inflow = W+Y*Z
    if total_inflow > X:
        print("overFlow")
    elif total_inflow == X:
        print("filled")
    elif total_inflow < X:
        print("Unfilled")

# Q4. Netflix
T = int(input())
for i in range(T):
    A, B, C, X = list(map(int, input().split()))
    if A+B >= X or B+C >= X or A+C >= X:
        print("YES")
    else:
        print("NO")

# Q5. Gold Mining
T = int(input())
for i in range(T):
    N, X, Y = list(map(int, input().split()))
    if (N+1)*Y >= X:
        print("YES")
    else:
        print("NO")
