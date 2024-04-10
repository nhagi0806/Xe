import numpy as np
import matplotlib.pyplot as plt
from ReImB import sigmaHe

E = np.linspace(0.1, 50, 1000)

sigmaHe = sigmaHe(E)

plt.figure(figsize=(8, 6))
plt.plot(E, sigmaHe, label='sigma(E)')
plt.title('sigma(E)')
plt.xlabel('E')
plt.ylabel('sigma(E)')
plt.grid(True)
plt.legend()

plt.savefig('sigmaHe.png')
plt.show()
