import numpy as np
import matplotlib.pyplot as plt
import math
import const131
import const129
import constHe
import pandas as pd
import ReImB

E_values = np.linspace(1, 20, 100000)  
#E_values = np.linspace(0.01, 1, 100000)  #10meVから1eVまで

epsilon_values = ReImB.epsilon129(E_values)
#epsilon_values = ReImB.epsilon129_1atm(E_values)  #1atmセルでのグラフ
#epsilon_values = ReImB.epsilon129Poln(E_values)   #3atmでの中性子偏極率を入れたグラフ
#epsilon_values = ReImB.epsilon129Poln_1atm(E_values)   #1atmでの中性子偏極率を入れたグラフ

plt.plot(E_values, epsilon_values)
plt.xlabel('E')
plt.ylabel('epsilon129(E)')
plt.title('epsilon129(E) vs E')
plt.grid(True)
#plt.xscale('log')  #横軸log（10meVから1eVの範囲）

closest_index = np.argmin(np.abs(E_values - 9.57))

plt.text(9.57, ReImB.epsilon129(9.57), f'y={ReImB.epsilon129(9.57):.3g}', ha='right', va='bottom')
#plt.text(9.57, ReImB.epsilon129_1atm(9.57), f'y={ReImB.epsilon129_1atm(9.57):.3g}', ha='right', va='bottom')   #1atmセルでのグラフ
#plt.text(9.57, ReImB.epsilon129Poln(9.57), f'y={ReImB.epsilon129Poln(9.57):.3g}', ha='right', va='bottom')    #3atmでの中性子偏極率を入れたグラフ
#plt.text(9.57, ReImB.epsilon129Poln_1atm(9.57), f'y={ReImB.epsilon129Poln_1atm(9.57):.3g}', ha='right', va='bottom')    #1atmでの中性子偏極率を入れたグラフ
plt.savefig('asym_129Xe.png')  
#plt.savefig('asym_129Xe_1atm.png')  #1atmセルでのグラフ
#plt.savefig('asym_129XePoln.png')  #3atmでの中性子偏極率を入れたグラフ
#plt.savefig('asym_129XePoln_1atm.png')  #1atmでの中性子偏極率を入れたグラフ
#plt.savefig('asym_129XePoln10meV_1eV.png')  #10meVから1eVまで
#plt.savefig('asym_129XePoln10meV_1eV_1atm.png')  #10meVから1eVまで1atm

plt.show()  