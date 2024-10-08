import requests
import numpy as np
import pandas as pd


print('***REQVEST***')
print('---Получение заголовков страницы---')
r = requests.get('https://api.github.com/events')
print(r.headers)
print()
print('---Передача параметров в URL-адресах---')
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
print()
print('---запросы POST---')
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
print()
print('***NUMPY***')
print('---создания массива со значениями, равномерно распределёнными в '
      'заданном интервале---')
ar = np.linspace(0, 10, num=5)
print(ar)
print()
print('---Генерация случайных целых чисел---')
rng = np.random.default_rng()
ar =  rng.integers(9, size=(2, 5))
print(ar)
print('---Cглаживания массива---')
print(ar.flatten())
print()
print('***PANDAS***')
print('---Считывание из файла csv---')
df = pd.read_csv(f'./sample1.csv', delimiter=',')
print(df)
print()
print('---Выводим список меток столбцов---')
print(*df.columns)
print()
print('---1-ые 2 сторки в массив NumPy с немаркированными данными---')
print(df.head(2).to_numpy())