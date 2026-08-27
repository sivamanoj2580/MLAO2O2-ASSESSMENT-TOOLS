import random

trials = 1000
on_time = 0

for i in range(trials):
    traffic = random.choice(["Low", "Medium", "High"])

    if traffic in ["Low", "Medium"]:
        on_time += 1

probability = on_time / trials

print("Total Trials:", trials)
print("On-Time Deliveries:", on_time)
print("Estimated Probability:", probability)

print("U. Lakshmi Chenna Kesava Reddy - 192425206")
