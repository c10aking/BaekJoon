x, y, w, h = map(int, input().split())
dist = min(x, y, w-x, h-y)
print(dist)