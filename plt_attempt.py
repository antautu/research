import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [1, 2, 3]
x1 = [2, 4, 6]
y1 = [2, 4, 6]

ax1 = plt.subplot(2,1,1)
ax1.plot(x, y)
ax2 = plt.subplot(2,1,2, sharex=ax1)
ax2.plot(x1, y1)
plt.show()