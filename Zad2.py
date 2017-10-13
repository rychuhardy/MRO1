import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

samples_num = 100  # 00
dim_min = 1
dim_max = 100  # 0000
repetitions_num = 20
X = 1
results = {}

for dim in range(dim_min, dim_max + 1):
    for rep in range(0, repetitions_num):
        samples = np.random.uniform(0, 1, size=(samples_num, dim))
        distances = []
        for i in samples:
            for j in samples:
                if not (i == j).all():
                    distances.append(np.linalg.norm(i - j))
        if rep == 0:
            results[dim] = [np.std(distances) / np.mean(distances)]
        else:
            results[dim].append(np.std(distances) / np.mean(distances))
        print(results[dim])

x = np.fromiter(results.keys(), int)
y = np.fromiter(map(np.mean, results.values()), float)
e = np.fromiter(map(np.std, results.values()), float)
print(x)
print(y)
plt.rcParams["figure.figsize"] = [16, 9]
# plt.yticks(np.arange(y.min(), 1, 0.005))
ax = plt.axes()
ax.grid(color='gray', linestyle='-', linewidth=1)
ax.set_xlabel('Liczba wymiarow')
ax.set_ylabel('Stosunek odchylenia standardowego do sredniej odleglosci miedzy losowymi punktami')
plt.errorbar(x, y, e, marker='*', ecolor='red', elinewidth=2)
plt.show()