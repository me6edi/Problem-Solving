
n = int(input())
arr = map(int, input().split())
myarr = set(arr)
myarr.remove(max(myarr))
print(max(myarr))