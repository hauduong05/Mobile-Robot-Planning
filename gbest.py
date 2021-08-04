import random
from objective_func import *


def tournament_selection(archive, p, r, Obstacles):
    s = set()
    best = archive[0]
    n = len(archive)
    while len(s) < n:
        choice = random.choices(range(n), k=2)
        a = [archive[choice[0]], archive[choice[1]]]
        s.update(choice)
        if dominate(a[0], a[1], p, r, Obstacles):
            better = a[0]
        elif dominate(a[1], a[0], p, r, Obstacles):
            better = a[1]
        else:
            better = 0
        if better != 0 and dominate(better, best, p, r, Obstacles):
            best = better

    return best


def select_gbest(archive1, archive2, t, tmax, p, r, Obstacles):
    ps = 0.5 * (1 - t / tmax)
    if len(archive1) == 0:
        gbest = tournament_selection(archive2, p, r, Obstacles)
    elif len(archive2) == 0:
        gbest = tournament_selection(archive1, p, r, Obstacles)
    else:
        r = random.uniform(0, 1)
        if r <= ps:
            gbest = tournament_selection(archive2, p, r, Obstacles)
        else:
            gbest = tournament_selection(archive1, p, r, Obstacles)

    return gbest


def shortest_path(archive):
    path = archive[0]

    for i in archive:
        if length_path(i) < length_path(path):
            path = i

    return path

def best_path(archive, p, r):
    paths = []
    for i in archive:
        dmin, dmax = danger(p, r, i)
        if dmin > 0:
            paths.append(i)

    bestpath = shortest_path(paths)
    return bestpath