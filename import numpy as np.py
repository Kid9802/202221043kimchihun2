import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
num = [100]
den = [1, 5, 6]  # 폐루프 전달함수의 분모

G = signal.TransferFunction(num, den)
t, y = signal.step(G)
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()
w, mag, phase = signal.bode(G)
plt.figure()
plt.semilogx(w, mag)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.title('Bode Diagram - Magnitude')
plt.grid(True)

plt.figure()
plt.semilogx(w, phase)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Phase [degrees]')
plt.title('Bode Diagram - Phase')
plt.grid(True)

plt.show()