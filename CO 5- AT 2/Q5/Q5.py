states = ["Start", "A", "B", "Goal"]
policy = {
    "Start": "Right",
    "A": "Right",
    "B": "Right"
}
rewards = {
    "Start": 0,
    "A": 0,
    "B": 0,
    "Goal": 10
}
value = {s: 0 for s in states}
gamma = 0.9
for _ in range(10):
    for s in states[:-1]:
        next_state = {
            "Start": "A",
            "A": "B",
            "B": "Goal"
        }[s]

        value[s] = rewards[s] + gamma * value[next_state]
for s in states[:-1]:
    policy[s] = "Right"
print("State Values:")
print(value)
print("\nOptimal Policy:")
for s in states[:-1]:
    print(s, "->", policy[s])
print("Goal -> STOP")

print(" U. Lakshmi Chenna Kesava Reddy - 192425206")
