import redis
import random

# Подключение к Redis
r = redis.Redis(host='localhost', port=6380, db=0)

# Создание 10 переменных с случайными значениями
for i in range(1, 10):
    r.set(f"variable:{i}", random.randint(0, 99))

# Проверка созданных переменных
for i in range(1, 11):
    print(f"variable:{i} = {r.get(f'variable:{i}')}")



import redis

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Получение всех ключей
keys = r.keys('*')

# Показ всех ключей и их значений
for key in keys:
    value = r.get(key)
    print(f'Key: {key.decode("utf-8")}, Value: {value.decode("utf-8") if value else None}')