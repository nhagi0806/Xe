import numpy as np
import matplotlib.pyplot as plt
from ReImB import Poln

E_values = np.linspace(0.1, 50, 1000)

Poln_values = Poln(E_values)

plt.figure(figsize=(8, 6))
plt.plot(E_values, Poln_values, label='Poln(E)')
plt.title('Poln(E)')
plt.xlabel('E')
plt.ylabel('Poln(E)')
plt.grid(True)
plt.legend()

closest_index_1441 = np.argmin(np.abs(E_values - 14.41))
closest_index_957 = np.argmin(np.abs(E_values - 9.57))

plt.text(14.41, Poln_values[closest_index_1441], f'y={Poln_values[closest_index_1441]:.3g}', ha='left', va='bottom')
plt.text(9.57, Poln_values[closest_index_957], f'y={Poln_values[closest_index_957]:.3g}', ha='left', va='bottom')

plt.savefig('Poln.png')
plt.show()
