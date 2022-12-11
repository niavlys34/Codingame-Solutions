import sys
import math

class Point:
    def __init__(self, slon: str, slat: str) -> None:
        self.lon = float(slon.replace(',', '.'))
        self.lat = float(slat.replace(',', '.'))

def distance(a: Point, b: Point) -> float:
    x = (b.lon - a.lon) * math.cos((a.lat + b.lat)/2)
    y = b.lat - a.lat
    return math.sqrt(x ** 2 + y ** 2) * 6371

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()

user_point = Point(lon, lat)

closest = ''
min_dist = -1

n = int(input())
for i in range(n):
    _, defib_name, _, _, defib_lon, defib_lat = input().split(';')
    defib_point = Point(defib_lon, defib_lat)
    dist = distance(user_point, defib_point)
    if dist < min_dist or min_dist == -1:
        closest = defib_name
        min_dist = dist

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(closest)
