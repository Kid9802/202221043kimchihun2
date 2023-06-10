import streamlit as st
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Iris 데이터셋 로드
iris = load_iris()
X = iris.data
y = iris.target

# k-NN 알고리즘 적용
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# 새로운 데이터 예측
new_data = [[5.1, 3.5, 1.4, 0.2]]
predicted_class = knn.predict(new_data)

# 결과 출력
st.write("Predicted class for new data:", predicted_class)