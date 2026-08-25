grid = [["S", ".", "."],
        [".", "#", "."],
        [".", ".", "G"]]

row, col = 0, 0
battery = 30
reward = 0
moves = ["Right", "Right", "Down", "Down"]

print("Starting Position: S")

for move in moves:
    if move == "Right":
        col += 1
    elif move == "Left":
        col -= 1
    elif move == "Up":
        row -= 1
    elif move == "Down":
        row += 1

    battery -= 1
    reward += 5
    print("Move:", move)

print("Destination:", grid[row][col])
print("Moves Used:", len(moves))
print("Battery Left:", battery)
print("Reward Earned:", reward)
print("Robot Reached Goal Successfully")

print("U.lakshmi Chenna Kesava Reddy - 192425206")
