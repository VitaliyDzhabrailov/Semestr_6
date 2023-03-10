"""
Вам на вход приходит большая матрица из целых чисел. Логически это карта. Каждый элемент матрицы - клеточка карты.
Значение элемента - высота над уровнем моря в данной клеточке (если число положительное) или
глубина моря (если число отрицательное). Размеры карты - до 1024 по каждой из сторон.

Необходимо найти:

1. общую площадь клеточек моря, в которых его глубина больше 5;
2. общий объём всей воды на карте;
3. максимальную высоту над уровнем моря, которая есть на этой карте.

Формат входных данных
В первой строке 2 целых числа - N и M. Далее N строк, в каждой по M целых чисел через пробел.

(Внимание: кто-то особо добрый отформатировал ввод так, что его удобно читать глазами.
Но в итоге между соседними числами бывает разное количество пробелов. С этим придётся справиться.)

Формат выходных данных
Три строки с целыми числами. В каждой - ответ на соответственный вопрос.
"""


import pandas as pd
n, m = map(int, input().split())
df = pd.DataFrame()
for i in range(n):
    df[i] = list(map(int, input().split()))

df_1 = df < -5
print(df_1.sum().sum())

df_2 = df <= -1
print((df_2 * df).sum().sum() * (-1))

print(df.max().max())