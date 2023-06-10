# 필요한 패키지 임포트
import numpy as np
import streamlit as st
from sklearn.cluster import KMeans

# 예시 데이터 생성
data = np.array([[2, 3], [3, 5], [1, 8], [6, 4], [7, 3], [6, 2]])

# k-means 클러스터링 함수
def kmeans_clustering(data, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return labels, centroids

# Streamlit 앱 구성
def main():
    st.title("K-means Clustering with Streamlit")
    st.write("Example data:")
    st.write(data)

    k = st.slider("Select the number of clusters (k):", min_value=2, max_value=10, value=3)
    labels, centroids = kmeans_clustering(data, k)

    st.write("Cluster labels:")
    st.write(labels)

    st.write("Cluster centroids:")
    st.write(centroids)

if __name__ == "__main__":
    main()