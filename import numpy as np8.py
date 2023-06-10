import numpy as np
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# 예시 데이터 생성
data = np.random.randn(100, 2)

# k-NN 알고리즘을 사용하여 iris 분류
iris = load_iris()
X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# k-means 클러스터링 함수
def kmeans_clustering(data, k):
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    kmeans = KMeans(n_clusters=k, init=centroids, n_init=1)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return labels, centroids

# Streamlit 앱 구성
def main():
    st.title("Iris Classification and K-means Clustering")
    st.subheader("k-NN Algorithm for Iris Classification")
    st.write("Example data:")
    st.write(data)

    new_data = np.array([[5.1, 3.5, 1.4, 0.2]])
    predicted_class = knn.predict(new_data)
    st.write("Predicted class for new data:", predicted_class)

    st.subheader("k-means Clustering")
    k = st.slider("Select the number of clusters (k):", min_value=2, max_value=10, value=3)
    labels, centroids = kmeans_clustering(data, k)

    st.write("Cluster labels:")
    st.write(labels)

    st.write("Cluster centroids:")
    st.write(centroids)

if __name__ == "__main__":
    main()