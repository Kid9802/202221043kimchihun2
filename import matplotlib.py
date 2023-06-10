import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 그래프 그리기
plt.plot(x, y)

# 그래프 제목 설정
plt.title("Simple Line Graph")

# x축 레이블 설정
plt.xlabel("X-axis")

# y축 레이블 설정
plt.ylabel("Y-axis")

# 그래프 표시
plt.show()