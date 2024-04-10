import numpy as np
import matplotlib.pyplot as plt
import math
import const131
import const129
import constHe
import pandas as pd
import ReImB

E_values = np.linspace(1, 20, 100000)  
#E_values = np.linspace(1, 4, 1000)  #E=3.0eVを見る
#E_values = np.linspace(0.01, 1, 100000)  #10meVから1eVまで

epsilon_values = ReImB.epsilon131(E_values)
#epsilon_values = ReImB.epsilon131_1atm(E_values)    #1atm
#epsilon_values = ReImB.epsilon131Poln(E_values)    #3atmで中性子偏極率あり
#epsilon_values = ReImB.epsilon131Poln_1atm(E_values)    #1atmで中性子偏極率あり

plt.plot(E_values, epsilon_values)
plt.xlabel('E')
plt.ylabel('epsilon131(E)')
plt.title('epsilon131(E) vs E')
plt.grid(True)
#plt.xscale('log')  #横軸log（10meVから1eVの範囲）

closest_index = np.argmin(np.abs(E_values - 14.41))
closest_index = np.argmin(np.abs(E_values - 3.20))

plt.text(14.41, ReImB.epsilon131(14.41), f'y={ReImB.epsilon131(14.41):.3g}', ha='right', va='bottom')
plt.text(3.20, ReImB.epsilon131(3.20), f'y={ReImB.epsilon131(3.20):.3g}', ha='right', va='bottom')
#plt.text(14.41, ReImB.epsilon131_1atm(14.41), f'y={ReImB.epsilon131_1atm(14.41):.3g}', ha='right', va='bottom')   #1atm
#plt.text(3.20, ReImB.epsilon131_1atm(3.20), f'y={ReImB.epsilon131_1atm(3.20):.3g}', ha='right', va='bottom')     #1atm
#plt.text(14.41, ReImB.epsilon131Poln(14.41), f'y={ReImB.epsilon131Poln(14.41):.3g}', ha='right', va='bottom')   #3atmで中性子偏極率あり
#plt.text(3.20, ReImB.epsilon131Poln(3.20), f'y={ReImB.epsilon131Poln(3.20):.3g}', ha='right', va='bottom')    #3atmで中性子偏極率あり
#plt.text(14.41, ReImB.epsilon131Poln_1atm(14.41), f'y={ReImB.epsilon131Poln_1atm(14.41):.3g}', ha='right', va='bottom')   #1atmで中性子偏極率あり
#plt.text(3.20, ReImB.epsilon131Poln_1atm(3.20), f'y={ReImB.epsilon131Poln_1atm(3.20):.3g}', ha='right', va='bottom')    #1atmで中性子偏極率あり
plt.savefig('asym_131Xe.png')
#plt.savefig('asym_131Xe_1atm.png')   #1atm  
#plt.savefig('asym_131Xe3.0.png')  #3.0eVにズーム
#plt.savefig('asym_131XePoln.png')   #3atmで中性子偏極率あり
#plt.savefig('asym_131XePoln_1atm.png')   #1atmで中性子偏極率あり
#plt.savefig('asym_131XePoln10meV_1eV.png')  #10meVから1eVまで
#plt.savefig('asym_131XePoln10meV_1eV_1atm.png')  #10meVから1eVまで1atm
plt.show()  