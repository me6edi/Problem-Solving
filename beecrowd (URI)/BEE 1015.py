import math
x1 , y1 = map(float, input().split())
x2 , y2 = map(float, input().split())
distance = ((x2 - x1)**2 + (y2 - y1)**2)
print("%.4f" % math.sqrt(distance))