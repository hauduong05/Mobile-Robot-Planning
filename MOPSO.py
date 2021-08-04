import random
from objective_func import *
from Point import *
from gbest import *
from update import *
import numpy as np


def Particle(n, y):
    Particle = []
    Vel = []
    for i in range(n):
        Particle.append(y + random.uniform(-1e-2, 1e-2))
        Vel.append(random.uniform(-1e-1, 1e-1))

    return Particle, Vel


def MOPSO(st, tg, p, r, Obstacles, ang):
    Ns = 50
    it_max = 10
    Na = 10
    Nas = 10
    t = 0
    Tmax = 100 * len(Obstacles)
    n = 10
    Swarm = []
    Partis = []
    vels = []
    pbest = []

    feasible_archive = []
    infeasible_archive = []
    for i in range(Ns):
        parti, v = Particle(n, st.y)
        Partis.append(parti)
        vels.append(v)
        points = Points(st, tg, n, parti)
        pbest.append(points)
        Swarm.append(points)
        feasible_archive, infeasible_archive = update_archive(Swarm[i], feasible_archive, infeasible_archive, Na, Nas,
                                                              Obstacles, p, r)

    while t < Tmax:
        gbest = select_gbest(feasible_archive, infeasible_archive, t, Tmax, p, r, Obstacles)
        for i in range(Ns):

            Partis[i], Swarm[i] = update_position(Partis[i], vels[i], Swarm[i], pbest[i], gbest, it_max, n,
                                                      Obstacles,
                                                      ang)
            if dominate(Swarm[i], pbest[i], p, r, Obstacles):
                pbest[i] = Swarm[i]
            feasible_archive, infeasible_archive = update_archive(Swarm[i], feasible_archive, infeasible_archive, Na,
                                                                  Nas,
                                                                  Obstacles, p, r)
        t += 1

    path = shortest_path(feasible_archive)
    bestpath = best_path(feasible_archive, p, r)

    return path, bestpath

