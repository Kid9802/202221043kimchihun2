import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# 폐루프 전달함수 H(s)
num = [1, 5, 6]  # (s+2)(s+3)
den = [100]  # 100

# 시스템 응답 계산
t, y = signal.step(signal.TransferFunction(num, den))

# 시간 영역 응답 그래프
plt.figure(figsize=(8, 6))
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Step Response')
plt.title('Step Response of Closed-Loop System')
plt.grid(True)
plt.show()

# 주파수 영역 응답 보드선도
w, mag, phase = signal.bode(signal.TransferFunction(num, den))

plt.figure(figsize=(8, 6))
plt.semilogx(w, mag)  # 주파수 응답 그래프
plt.xlabel('Frequency')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot - Magnitude Response')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.semilogx(w, phase)  # 위상 응답 그래프
plt.xlabel('Frequency')
plt.ylabel('Phase (degrees)')
plt.title('Bode Plot - Phase Response')
plt.grid(True)
plt.show()