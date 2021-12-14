"""
K-means impl, take square for example
@Author: JiananYuan
@Date: 2021/12/14
"""
import random
import matplotlib.pyplot as plt


def check_consistent(last_cluster, current_cluster):
    """
    check whether last_cluster is the same as current_cluster
    :param: last_cluster [[ ]]
    :param: current_cluster [[ ]]
    :return: is_consistent  --bool
    """
    if len(last_cluster) != len(current_cluster):
        return False
    lenc = len(current_cluster)
    for i in range(0, lenc):
        if len(last_cluster[i]) != len(current_cluster[i]):
            return False
        lencc = len(last_cluster[i])
        for j in range(0, lencc):
            if last_cluster[i][j] != current_cluster[i][j]:
                return False
    return True


def calculate_dis(point_1, point_2):
    """
    calculate the distance between point_1 and point_2
    @param: point_1 []
    @param: point_2 []
    @return: square distance  --float64
    """
    return pow((point_1[0] - point_2[0]), 2) + pow((point_1[1] - point_2[1]), 2)


def kmeans(data, K):
    """
    kmeans kernel function
    :param: data  -- [[ ]]
    :param: K  -- number of clusters
    :return: clusters  -- [[ ]]
    """
    # how many points
    lent = len(data)
    # how many points does a segment contains
    lens = lent // K
    # center of clusters
    centers = []
    for i in range(0, K):
        centers.append(data[random.randint(i * lens, (i + 1) * lens - 1)])
    # clusters set
    clusters = []
    for i in range(0, K):
        clusters.append([])
    last_clusters = []
    while not check_consistent(last_clusters, clusters):
        last_clusters = clusters
        for i in range(0, K):
            clusters[i].clear()
        # dis: [[]]  -- dis[i][j]: distance between centers[i] and data[j]
        dis = []
        for i in range(0, K):
            dis.append([])
        # calculate distance between each cluster
        for i in range(0, lent):
            for j in range(0, K):
                dis[j].append(calculate_dis(centers[j], data[i]))
        # classify point into corresponding cluster
        for i in range(0, lent):
            max_dis = 99999999999999999999999999999999
            max_dis_id = -1
            for j in range(0, K):
                if dis[j][i] < max_dis:
                    max_dis = dis[j][i]
                    max_dis_id = j
            clusters[max_dis_id].append(data[i])
        # current clusters have generated, now calculate new centers
        new_clusters_center_x = []
        new_clusters_center_y = []
        len_clusters = []
        for i in range(0, K):
            len_clusters.append(len(clusters[i]))
            new_clusters_center_x.append(0)
            new_clusters_center_y.append(0)
        for i in range(0, K):
            for j in range(0, len_clusters[i]):
                new_clusters_center_x[i] += clusters[i][j][0]
                new_clusters_center_y[i] += clusters[i][j][1]
        for i in range(0, K):
            new_clusters_center_x[i] /= len_clusters[i]
            new_clusters_center_y[i] /= len_clusters[i]
            centers[i] = [new_clusters_center_x[i], new_clusters_center_y[i]]
    return last_clusters


def plot_cluster_result(clusters):
    """
    plot clusters result
    :param clusters: [[ ]]
    :return: none
    """
    pass


if __name__ == '__main__':
    data = [
        [0, 0], [1, 0],
        [6, 5], [5, 6],
        [3, 3], [3, 4]
    ]
    clusters = kmeans(data, 2)
    print(clusters)
