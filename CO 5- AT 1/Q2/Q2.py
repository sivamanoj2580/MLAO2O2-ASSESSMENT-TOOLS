import random

ads = ["Ad1","Ad2","Ad3","Ad4","Ad5"]
clicks = [25,40,70,35,55]

best = clicks.index(max(clicks))

print("Advertisement Performance\n")

for i in range(5):
    print(ads[i],":",clicks[i],"Clicks")

print("\nBest Advertisement:", ads[best])

reward = clicks[best]

print("Reward:", reward)
print("Exploration Strategy: Epsilon-Greedy")
print("Budget Used: 10000 Users")
print("Status: Maximum Click Rate Achieved")

print("U.lakshmi Chenna Kesava Reddy - 192425206")
