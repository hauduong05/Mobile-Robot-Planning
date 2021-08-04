from shapely.geometry import Point, LineString, MultiPoint, Polygon, MultiPolygon
from descartes import PolygonPatch
from Point import *
from MOPSO import *
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

test = "test.txt"
Obstacles = [ ]
obsta = [ ]

with open(test, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[ i ] = lines[ i ].rstrip().split(" ")
    st = MyPoint(float(lines[ 0 ][ 0 ]), float(lines[ 0 ][ 1 ]))
    tg = MyPoint(float(lines[ 1 ][ 0 ]), float(lines[ 1 ][ 1 ]))
    p = MyPoint(float(lines[ 2 ][ 0 ]), float(lines[ 2 ][ 1 ]))
    r = float(lines[ 2 ][ 2 ])
    num_obs = int(lines[ 3 ][ 0 ])
    n_obs = [ int(i) for i in lines[ 4 ] ]
    lines = lines[ 5: ]
    lines = [ MyPoint(float(j[ 0 ]), float(j[ 1 ])) for j in lines ]
    for i in range(num_obs):
        t = n_obs[ i ]
        Obstacles.append(lines[ :t ])
        lines = lines[ t: ]

angle = angle(st, tg)
st_r = st.rotate(angle)
tg_r = tg.rotate(angle)

p_r = p.rotate(angle)
Obstacles_r = [ ]
obs = [ ]

for i in range(num_obs):
    obs_r = [ ]
    obs = [ ]
    for j in range(n_obs[ i ]):
        obs_r.append(Obstacles[ i ][ j ].rotate(angle))
        obs.append([ Obstacles[ i ][ j ].x, Obstacles[ i ][ j ].y ])
    Obstacles_r.append(obs_r)
    obsta.append(obs)

path, best_path = MOPSO(st_r, tg_r, p_r, r, Obstacles_r, -angle)

Path = []
Best_Path = []
line_x = []
line_y = []

for i in path:
    k = i.rotate(-angle)
    Path.append(k)

for i in best_path:
    k = i.rotate(-angle)
    Best_Path.append(k)
    line_x.append(k.x)
    line_y.append(k.y)

print(length_path(best_path))
print(length_path(path))


fig, ax = plt.subplots()

for i in range(num_obs):
    pt = Polygon(obsta[ i ], facecolor='k')
    ax.add_patch(pt)

plt.plot(line_x, line_y, 'r')
ax.set_xlim([ 0, 50 ])
ax.set_ylim([ 0, 50 ])

circle = plt.Circle((p.x, p.y), r)
ax.add_patch(circle)
plt.show()
