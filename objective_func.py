from shapely.geometry import LineString, Polygon


def length_path(points):
    line = LineString(points)
    return line.length


def danger(p, r, points):
    line = LineString(points)
    d = p.distance(line)
    danmax = r + d
    if r < d:
        danmin = d - r
    else:
        danmin = 0
    return (danmin, danmax)


def collision(points, Obstacles):

    d = 0
    line = LineString(points)
    n = len(Obstacles)
    for i in range(n):
        polygon = Polygon(Obstacles[i])
        if line.distance(polygon) < 1e-2:
            d += 1

    return d / n


def dominate(points1, points2, p, r, Obstacles):
    l1, l2 = length_path(points1), length_path(points2)
    dmin1, dmax1 = danger(p, r, points1)
    dmin2, dmax2 = danger(p, r, points2)
    cv1, cv2 = collision(points1, Obstacles), collision(points2, Obstacles)
    c = 0
    if (dmin1 > dmin2 and dmax1 >= dmax2) or (dmin1 >= dmin2 and dmax1 > dmax2):
        c = 1
    if cv1 < cv2:
        return True
    elif cv1 == cv2 and c == 1 and l1 <= l2:
        return True
    elif cv1 == cv2 and dmin1 == dmin2 and dmax1 == dmax2 and l1 < l2:
        return True
    elif cv1 == cv2 and ((dmin1 - dmin2) * (dmax1 - dmax2) < 0) and l1 < l2:
        return True
    elif cv1 == cv2 and dmin1 > 0 and dmin2 > 0 and l1 < l2:
        return True
    return False
