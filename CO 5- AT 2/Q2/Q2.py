import random

movies = ["Movie1", "Movie2", "Movie3"]
rewards = [0, 0, 0]
counts = [0, 0, 0]
epsilon = 0.1

user_rewards = [5, 3, 4, 5, 2, 5, 4, 5, 3, 4]

for reward in user_rewards:

    if random.random() < epsilon:
        movie = random.randint(0, 2)
    else:
        movie = rewards.index(max(rewards))

    counts[movie] += 1
    rewards[movie] += reward

averages = [rewards[i] / counts[i] if counts[i] else 0
            for i in range(3)]

best = averages.index(max(averages))

print("Average Rewards:", averages)
print("Best Movie:", movies[best])

print("U. Lakshmi Chenna Kesava Reddy - 192425206")
