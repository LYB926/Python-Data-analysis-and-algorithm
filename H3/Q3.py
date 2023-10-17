# 3. 编写程序，实现对Flower.dat文件表示的图像用如下拉普拉斯算子进行空间滤波：
# np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
# 图像边缘采用复制填充方式，并以图片形式保存结果（uint8）

import numpy as np
from matplotlib import pyplot as plt

# 读取dat位图
FILE = open('Flower.dat', 'rb')
img = np.fromfile(FILE, dtype=np.uint8).reshape((1024, 1024))
FILE.close()

# 对图像的边缘采取复制填充
img_padded = np.pad(img, 1, mode='edge')
# print(img_padded.shape)

# 使用拉普拉斯卷积核进行卷积以锐化图像
kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
img_edge = np.empty((1024, 1024), dtype=np.int16)
for i in range(1, 1025):
    for j in range(1, 1025):
        pixel = img_padded[i-1:i+2, j-1:j+2] * kernel
        img_edge[i-1, j-1] = pixel.sum()

# 将原始图像和边缘叠加，并使用np.clip()截断到uint8范围，得到锐化后的图像
img_enhanced = np.clip(img + img_edge, 0, 255)
plt.imsave('img_enhanced.png', img_enhanced, cmap='gray')

# 显示图像
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.subplot(1, 3, 2)
plt.imshow(img_edge, cmap='gray')
plt.title('Filtered Image')
plt.subplot(1, 3, 3)
plt.imshow(img_enhanced, cmap='gray')
plt.title('Enhanced Image')
plt.show()