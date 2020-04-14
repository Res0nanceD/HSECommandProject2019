import json
from flask import Flask, request
from flask_restful import reqparse, Api, Resource
from agg import AgglomerativeClustering

app = Flask(__name__)
api = Api(app)

experiments = {}

# получение данных
point_list = []
file_name = 'data.json'
with open(file_name, 'r') as f:
    incoming_data = json.load(f)

class Experiment(Resource):

    # http://127.0.0.1/experiments/get<int:exp_id>
    # показывает результат эксперимента<int:exp_id>
    def get(self, exp_id):
        if exp_id not in experiments:
            return "Experiment does not exist", 404
        return experiments[exp_id]

    # http://127.0.0.1/experiments/post<number_of_clusters>
    # создает новый эксперимент
    def post(self, number_of_clusters):
        # добавляет новый эксперимент в словарь experiments
        exp_id = len(experiments) + 1
        experiments[exp_id] = {}
        # парсит запрос на нужные данные для алгоритма кластеризации
        parser = reqparse.RequestParser()
        parser.add_argument('number_of_clusters', help='число кластеров', type=int)
        args = parser.parse_args()
        result = AgglomerativeClustering(point_list, number_of_clusters)
        # Вобавляет результат к ключу
        experiments[exp_id] = result
        # Выводит результат
        return result, 201


class ExperimentList(Resource):
    # http://127.0.0.1/experiments/
    # возращает список экспериментов
    def get(self):
        return experiments


api.add_resource(ExperimentList, '/experiments')
api.add_resource(Experiment, '/experiments/<number_of_clusters>', '/experiments/<exp_index>')

if __name__ == '__main__':
    app.run()
