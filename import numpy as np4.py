import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# 전달 함수 G(s)
num = [100]
den = [1, 5, 6]  # (s+2)(s+3)

# 폐루프 전달 함수 계산
closed_loop_tf = signal.TransferFunction(num, den)

# unit step 입력의 응답 계산
t, y = signal.step(closed_loop_tf)

# 응답 곡선 그리기
plt.figure(figsize=(8, 6))
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response of Closed-Loop System')
plt.grid(True)
plt.show()

# 주파수 응답 그리기
w, mag, phase = signal.bode(closed_loop_tf)

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