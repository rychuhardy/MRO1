import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

samples_num = 1000 #00
dim_min = 1
dim_max = 25 #0000
repetitions_num = 20
X = 1
results = {}

for dim in range(dim_min, dim_max + 1):
    for rep in range(0, repetitions_num):
        samples = np.random.uniform(-X, X, size=(samples_num, dim))
        distances = map(lambda x: np.linalg.norm(x), samples)
        outliers_count = sum(1 for i in distances if i <= X)
        outliers_avg = outliers_count / samples_num
        if rep == 0:
            results[dim] = [outliers_avg]
        else:
            results[dim].append(outliers_avg)
    #print(np.std(results[dim]), np.mean(results[dim]))
#print(results)
x = np.fromiter(results.keys(), int)
y = np.fromiter(map(np.mean, results.values()), float)
e = np.fromiter(map(np.std, results.values()), float)

plt.rcParams["figure.figsize"] = [16,9]
#plt.yticks(np.arange(y.min(), 1, 0.005))
ax = plt.axes()
ax.grid(color='gray', linestyle='-', linewidth=1)
ax.set_xlabel('Liczba wymiarow')
ax.set_ylabel('Procent punktów w hiperkuli')
plt.errorbar(x, y, e, marker='*', ecolor='red', elinewidth=2)
plt.show()