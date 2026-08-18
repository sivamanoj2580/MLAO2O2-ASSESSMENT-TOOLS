import numpy as np

img = np.array([
    [10,20,30],
    [20,100,40],
    [30,40,50]
])

new = img.copy()

new[1,1] = np.mean([
    img[0,1],
    img[2,1],
    img[1,0],
    img[1,2]
])

print("Original Image:")
print(img)

print("\nUpdated Image:")
print(new)
