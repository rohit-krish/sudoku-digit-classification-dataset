import os
import matplotlib.pyplot as plt

data = {}

for i in range(9):
    data[str(i)] = len(os.listdir("./"+str(i)))


plt.bar(range(9), list(data.values()))
plt.title("Total: "+str(sum(list(data.values()))))
plt.show()

