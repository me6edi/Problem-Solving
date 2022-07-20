
a = int(input())
a1 = set(map(int,input().split()))
n = int(input())
n1 = set(map(int,input().split()))

ans = a1.union(n1)
count = 0
for i in ans:
    count = count + 1
print(count)