import numpy as np
import matplotlib.pyplot as plt

# tanh関数の定義
def tanh(E):
    return np.tanh(1/np.sqrt(E))

# -10から10までの値の範囲を生成
E = np.linspace(1, 10, 400)

# 範囲内の各値に対してtanhを計算
tanh_E = tanh(E)

# 関数をプロット
plt.figure(figsize=(8, 6))
plt.plot(E, tanh_E, label='tanh(E)')
plt.title('tanh(E)')
plt.xlabel('E')
plt.ylabel('tanh(E)')
plt.grid(True)
plt.legend()
plt.show()
