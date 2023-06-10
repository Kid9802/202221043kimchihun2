import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 전달함수 정의
num = [100]
den = [1, 5, 6]  # 폐루프 전달함수의 분모

# 폐루프 전달함수 계산
G = signal.TransferFunction(num, den)

# Unit step 입력에 대한 응답 곡선 계산
t, y = signal.step(G)

# 주파수 응답 보드선도 계산
w, mag, phase = signal.bode(G)

# 응답 곡선 그리기
plt.figure()
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()

# 주파수 응답 보드선도 그리기
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