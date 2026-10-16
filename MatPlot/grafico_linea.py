# pip install matplotlib #

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,5,10,25,38]

plt.plot(x, y, color="purple")
plt.title("Grafico a Linee")
plt.xlabel("Label X")
plt.ylabel("Label Y")
plt.grid(visible=True, which="both", axis="both")
plt.show()