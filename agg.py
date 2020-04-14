# agglomerative clustering, метод одиночной связи
#import json


class Cluster():

    def __init__(self, elements_of_cluster):
        self.elements_of_cluster = elements_of_cluster
        self.experiment_id = None

    def show_elements(self):
        return self.elements_of_cluster

    def unite_cluster(self, other_cluster):
        for elem in other_cluster.show_elements():
            self.elements_of_cluster.append(elem)


def distance_function(x):
    return ((x[0][0] - x[1][0]) ** 2 + (x[0][1] - x[1][1]) ** 2) ** .5


def find_cluster(point, cluster_list):
    for cluster in cluster_list:
        for elem in cluster.show_elements():
            if elem == point:
                return cluster


def find_cluster_and_index(point, cluster_list):
    for index in range(len(cluster_list)):
        for elem in cluster_list[index].show_elements():
            if elem == point:
                return [cluster_list[index], index]


# получение данных
# point_list = []
# file_name = 'data.json'
# with open(file_name, 'r') as f:
#     incoming_data = json.load(f)

# число кластеров
# n = incoming_data[0]
# for elem in incoming_data[1:]:
#     point_list.append(elem)


def AgglomerativeClustering(point_list, n):
    # поиск всех возможных пар точек
    length_list = []
    for i in range(len(point_list)):
        for j in range(i + 1, len(point_list)):
            length_list.append([point_list[i], point_list[j]])

    # сортировка пар точек по увеличеню расстояния
    length_list = sorted(length_list, key=lambda x: distance_function(x))

    # 1 шаг алгоритма
    cluster_list = []
    for elem in point_list:
        a = list()
        a.append(elem)
        a = Cluster(a)
        cluster_list.append(a)

    # шаги алгоритма кластеризации
    i = 0
    j = 0
    while i <= (len(point_list) - n - 1):
        a = find_cluster(length_list[j][0], cluster_list)
        b, index = find_cluster_and_index(length_list[j][1], cluster_list)
        if a != b:
            a.unite_cluster(b)
            cluster_list.pop(index)
            i += 1
        j += 1
    return cluster_list


# вывод полученных данных
# cluster_list = AgglomerativeClustering(point_list)
# def output(cluster_list):
#     for i in range(len(cluster_list)):
#         print(i + 1, ' '.join(str(i) for i in cluster_list[i].show_elements()))
