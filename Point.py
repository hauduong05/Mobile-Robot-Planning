from shapely.geometry import Point, LineString, MultiPoint, Polygon, MultiPolygon
import numpy as np
from math import *

class MyPoint(Point):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setX(self, x):
        return MyPoint(x, self.y)

    def setY(self, y):
        return MyPoint(self.x, y)

    def getxy(self):
        return self.x, self.y

    def rotate(self, angle):

        c, s = np.cos(angle), np.sin(angle)
        r_matrix = np.array([[c, -s], [s, c]])
        new_xy = list(np.matmul(r_matrix, self.getxy()))
        return MyPoint(new_xy[0], new_xy[1])

def angle(p1, p2):
    cos_angle = (p2.x - p1.x) / (hypot((p2.x - p1.x), (p2.y - p1.y)))

    angle = acos(cos_angle)

    if (p2.x - p1.x) * (p2.y - p1.y) > 0:
        if angle < pi / 2:
            return -angle
        else:
            return angle
    elif (p2.x - p1.x) * (p2.y - p1.y) < 0:
        if angle < pi / 2:
            return angle
        else:
            return -angle
    else:
        return angle

def Points(st, tg, n ,Particle):

    points = []
    points.append(st)
    d = st.distance(tg)/ (n + 1)
    for i in range(1, n + 1):
        if st.x < tg.x:
          points.append(MyPoint(st.x + i * d, Particle[i - 1]))
        else:
          points.append(MyPoint(st.x - i * d, Particle[i - 1]))
    points.append(tg)

    return points
