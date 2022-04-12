from random import randint

students = ['Денис', 'Дима', 'Ваня', 'Дима', 'Дима', 'Лёха', 'Вова', 'Вадим', 'Богдан', 'Юра', 'Антон', 'Артем', 'Костя']
math = [randint(25, 50) for i in range(13)]
physics = [randint(25, 50) for i in range(13)]
english = [randint(25, 50) for i in range(13)]
grades = list(map(lambda x, y, z: x + y + z, math, physics, english))
print([students[i] for i in range(13) if grades[i] >= 100])