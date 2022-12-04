import matplotlib.pyplot as plt
import numpy as np

# 要素数を定義
num_x = 4
x = np.arange(1, num_x+1)
# print(x)

y_upper = np.random.randint(1, 10, num_x)
# print(y_upper)
# [9 3 1 8]

y_lower = np.random.randint(1, 10, num_x)
# print(y_lower)
# [2 9 8 9]

# グラフ作成
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.bar(x, y_lower, color='blue')
ax1.bar(x, y_upper, color='green')
ax1.set_ylim(0,20)
plt.savefig('false.png')
# plt.show()
plt.clf()
plt.close()

# グラフ作成
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.bar(x, y_lower, color='blue')
ax2.bar(x, y_upper, color='green', bottom=y_lower)
ax2.set_ylim(0,20)
plt.savefig('true.png')
# plt.show()
plt.clf()
plt.close()