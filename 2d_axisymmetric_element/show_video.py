import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # 导入3D绘图工具
import numpy as np
import read_quad_dat

# points = np.load('D:/pydtest/tetrahedron/points.npy')
points = read_quad_dat.getdata('axis_quad.dat')[0]
X = points[:, 0]
Y = points[:, 1]
Z = np.zeros(len(X))
# C0 = np.loadtxt('result.txt')
C0 = np.loadtxt('result.txt')


# 设置图表和坐标轴
fig = plt.figure()  # 创建一个图
ax = fig.add_subplot(111, projection='3d')

# 创建散点图
scatter = ax.scatter3D(X, Y, Z, c=C0[:, -1], cmap='jet')

# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


cb = plt.colorbar(scatter, ax=ax)


# 你的动画函数
def update(frame):
    # 在这里更新你的图表或动画内容
    # 这个函数会为每一帧调用
    # scatter._offsets3d = (X, Y, Z)  # 更新散点位置
    scatter.set_array(C0[:, frame])  # 更新颜色数据
    print(np.mean(C0[:, frame]))

    return scatter  # 返回一个可迭代的对象
    # plt.draw()

# 设置帧数
num_frames = 100

# 创建动画
ani = FuncAnimation(fig, update, frames=num_frames, interval=1)

# 显示图表（可选）
plt.show()

