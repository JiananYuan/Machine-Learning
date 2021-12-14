[K-Means聚类算法原理](https://www.cnblogs.com/pinard/p/6164214.html)

使用点集 `data = [
        [0, 0], [1, 0], [0, 1],
        [6, 5], [5, 6], [6, 6]
    ]`；

聚类结果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2979e1e43bcf487c839d4ae2bf08aabd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQW5keVp6en4=,size_18,color_FFFFFF,t_70,g_se,x_16)

加上生成数据集的代码：
```py
def generate_2d_points(n, x_min, x_max, y_min, y_max):
    """
    generate 2D points
    :param n: how many points
    :param x_range: range of X
    :param y_range: range of Y
    :return: random points  [[ ]]
    """
    data = []
    for i in range(0, n):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        data.append([x, y])
    return data
```

同时修改主函数代码（主要是修改生成数据）：
```py
if __name__ == '__main__':
    # data = [
    #     [0, 0], [1, 0], [0, 1],
    #     [6, 5], [5, 6], [6, 6]
    # ]
    data = generate_2d_points(100, 0, 300, 0, 300)
    data.extend(generate_2d_points(100, 500, 700, 500, 700))
    data.extend(generate_2d_points(100, 1000, 1200, 1000, 1200))
    clusters = kmeans(data, 3)
    # print(clusters)
    plot_cluster_result(clusters)

```

运行结果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/89572ac3ad0c4096b04a2b3a2d01e97b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQW5keVp6en4=,size_18,color_FFFFFF,t_70,g_se,x_16)
