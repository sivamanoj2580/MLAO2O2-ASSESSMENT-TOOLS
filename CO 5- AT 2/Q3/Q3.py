import numpy as np
grid = np.array([
    [0, 0, 0],
    [0, -1, 0],
    [0, 0, 10]
])
V = np.zeros((3,3))
gamma = 0.9
for _ in range(20):
    old = V.copy()
    for i in range(3):
        for j in range(3):
            if grid[i,j] == -1 or grid[i,j] == 10:
                continue
            values = []
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                x,y = i+di,j+dj

                if 0 <= x < 3 and 0 <= y < 3:
                    if grid[x,y] != -1:
                        values.append(grid[x,y] + gamma * old[x,y])

            V[i,j] = max(values)

print("Value Function:")
print(np.round(V,2))

print(" U. Lakshmi Chenna Kesava Reddy - 192425206")
