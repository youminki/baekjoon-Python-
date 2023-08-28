color = set()
name = set()
C, N = map(int, input().split())

for _ in range(C) :
    color.add(input())
for _ in range(N) :
    name.add(input())

Q = int(input())
for _ in range(Q) :
    X = input()
    
    ans = "No"
    for i in range(max(1, len(X) - 1005), min(len(X), 1005)) :
        if X[:i] in color and X[i:] in name :
            ans = "Yes"
            break
    print(ans)