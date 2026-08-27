states = ["S1", "S2", "S3", "Goal"]

V = {s: 0 for s in states}

alpha = 0.1
gamma = 0.9

# State transitions and rewards
data = [
    ("S1", 0, "S2"),
    ("S2", 0, "S3"),
    ("S3", 10, "Goal")
]

for s, r, next_s in data:
    V[s] = V[s] + alpha * (
        r + gamma * V[next_s] - V[s]
    )

print("State Values:")

for s in states:
    print(s, "=", round(V[s], 2))


print(" U. Lakshmi Chenna Kesava Reddy - 192425206")
