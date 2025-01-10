import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter


fig, ax = plt.subplots()


A = 1.0           
g = 0.2      
w = 2       
t = np.linspace(0, 15, 1000)  
A_t = A * np.exp(-g * t)

x_t = A * np.exp(-g * t) * np.cos(w * t)


ax.grid(True, which='both', linestyle='-', linewidth=1)

ax.plot(t, A_t, 'k', linestyle='--', 
        label ='Amplitude change in time', linewidth=0.9 )
ax.plot(t, - A_t, 'k', linestyle='--', linewidth=0.9) 
ax.plot(t, x_t, 'r', label=r'$x(t) = Ae^{-\gamma t} \cos(\omega t)$')

ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)


ax.set_xlabel('Time (t)')
ax.set_ylabel('Displacement (x)')
ax.set_title('Damped Harmonic Oscillation')
ax.legend()
ax.set_ylim(-1.3, 1.3)


ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
#plt.savefig("Damped_osicllation.png", format='png')

plt.show()

