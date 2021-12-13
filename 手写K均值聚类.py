# take 2-dimention for example
import random


def check_consistent(last_cluster, current_cluster):
    is_consistent = True
    if len(last_cluster) != len(current_cluster):
        return False
    lenc = len(current_cluster)
    # ...
    return is_consistent


def calculate_dis(point_1, point_2):
    return pow((point_1[0] - point_2[0]), 2) + pow((point_1[1] - point_2[1]), 2)


# 先以二分类为例
def kmeans(data, K):
    center_1 = data[random.randint(0, K // 2)]
    center_2 = data[random.randint(K // 2 + 1, K)]
    cluster_1 = [center_1]
    cluster_2 = [center_2]
    last_clusters = []
    lenc = len(data)
    while not check_consistent(last_clusters, [cluster_1, cluster_2]):
        dis_1 = []
        dis_2 = []
        for i in range(0, lenc):
            dis_1.append(calculate_dis(center_1, data[i]))
            dis_2.append(calculate_dis(center_2, data[i]))
        for i in range(0, lenc):
            if dis_1[i] <= dis_2[i]:
                cluster_1.append(data[i])
            else:
                cluster_2.append(data[i])
        new_cluster1_center_x = 0
        new_cluster1_center_y = 0
        new_cluster2_center_x = 0
        new_cluster2_center_y = 0
        len_cluster1 = len(cluster_1)
        len_cluster2 = len(cluster_2)
        for i in range(0, len_cluster1):
            new_cluster1_center_x += cluster_1[i][0]
            new_cluster1_center_y += cluster_1[i][1]
        for i in range(0, len_cluster2):
            new_cluster2_center_x += cluster_2[i][0]
            new_cluster2_center_y += cluster_2[i][1]
        new_cluster1_center_x /= len_cluster1
        new_cluster1_center_y /= len_cluster1
        new_cluster2_center_x /= len_cluster2
        new_cluster2_center_y /= len_cluster2
        center_1 = [new_cluster1_center_x, new_cluster1_center_y]
        center_2 = [new_cluster2_center_x, new_cluster2_center_y]
    return [cluster_1, cluster_2]
        

if __name__ == '__main__':
    data = [
        [0, 0], [1, 0], [0, 1],
        [6, 6], [6, 5], [5, 6]
    ]
    clusters = kmeans(data, 2)
    print(clusters)
