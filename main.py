import requests
from MainWindow import *
import sys
import json


def get_task():
    url = "https://dt.miet.ru/ppo_it_final"
    headers = {"X-Auth-Token": "mded552k"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Полетное задание получено")
        return response.text  # вывод полученных данных
    else:
        print("Ошибка при получении полетного задания")


def main():
    global result
    data = get_task()
    print(data)

    data_dict = json.loads(data)
    result = []
    for item in data_dict['message']:
        inner_arr = []
        for point in item['points']:
            inner_arr.append([point['SH'], point['distance']])
        result.append(inner_arr)


    print(result)


if __name__ == '__main__':
    main()
    app = QApplication(sys.argv)
    ex = MainWindow(result)
    ex.show()
    sys.exit(app.exec_())
