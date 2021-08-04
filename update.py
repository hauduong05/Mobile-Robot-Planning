from objective_func import *
import random
from Point import *


def check(t, ang):
    t_r = t.rotate(ang)
    if 0 <= t_r.y <= 50 and 0 <= t_r.x <= 50:
        return True
    return False


def update_archive(point, archive1, archive2, Na, Nas, Obstacles, p, r):
    cv = collision(point, Obstacles)
    if cv == 0:
        if len(archive1) < Na:
            archive1.append(point)
        else:
            for i in archive1:
                if dominate(point, i, p, r, Obstacles):
                    archive1.remove(i)
                    archive1.append(point)
                    break
    else:
        if len(archive2) < Nas:
            archive2.append(point)
        else:
            for i in archive2:
                if dominate(point, i, p, r, Obstacles):
                    archive2.remove(i)
                    archive2.append(point)
                    break

    return archive1, archive2


def update_position(Particle, Vel, points, pbest, gbest, it_max, n, Obstacles, ang):
    w = 0.8
    c1 = 2
    c2 = 2
    pb = []
    gb = []
    k = 0
    while k < n:
        pb.append(pbest[k + 1].y)
        gb.append(gbest[k + 1].y)
        k += 1

    j = 0
    while j < n:
        iter = 0
        r1 = random.uniform(0, 0.18)
        r2 = random.uniform(0, 0.18)
        v = w * Vel[j] + r1 * c1 * (pb[j] - Particle[j]) + r2 * c2 * (gb[j] - Particle[j])
        pos = Particle[j] + Vel[j]
        iter += 1
        if check(MyPoint(points[j + 1].x, pos), ang):
            Vel[j] = v
            Particle[j] = pos
        points[j + 1] = points[j + 1].setY(Particle[j])
        line = [points[j], points[j + 1]]
        while iter < it_max and collision(line, Obstacles) > 0:
            pm = (iter / it_max) ** 3
            r = random.uniform(0, 1)
            if pm <= r:
                iter += 1
                break
            else:
                range = 2 * pm
                t = Particle[j] + random.normalvariate(0, 1) * range
                if check(MyPoint(points[j + 1].x, t), ang):
                    Particle[j] = t
                    points[j + 1] = points[j + 1].setY(Particle[j])
                line = [points[j], points[j + 1]]
                if collision(line, Obstacles) > 0:
                    iter += 1

        j += 1

    return Particle, points


