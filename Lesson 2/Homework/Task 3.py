"""
У вас есть данные по разным играм и тому, как их оценивают пользователи.
По каждой игре известны название и студия-разработчик.
Для каждой игры есть какое-то количество оценок (для разных игр оно разное).


Требуется:

1. найти 3 игры с самой высокой средней оценкой,
вывести их названия и средние оценки в порядке убывания средней оценки;
2. найти студию-разработчика, у которой максимальное количество игр с рейтингом выше 8.0,
вывести название студии и количество таких игр у неё.


Формат входных данных
В первой строке приходит путь к csv-файлу, в котором хранятся данные об играх.
По каждой игре в файле содержатся её идентификационный номер, название игры, название студии-разработчика.

Во второй строке приходит путь к файлу, в котором хранятся данные об оценках.
В файле дано множество оценок игр пользователями в формате "идентификационный номер игры - оценка".


Формат выходных данных
В первых трёх строках 3 самые популярные игры.
У каждой название и через пробел средняя оценка строго с тремя знаками после запятой.
В четвёртой строке название лучшей студии-разработчика, после названия через пробел количество рейтинговых игр.
"""

import pandas as pd

df_games_path = str(input())
df_rates_path = str(input())

df_games = pd.read_csv(df_games_path, sep=";")
df_rates = pd.read_csv(df_rates_path, sep=";")

df_rates_mean = df_rates.groupby(['id'], as_index=False).mean()
df_rates_mean.sort_values(by='mark', ascending=False, inplace=True, ignore_index=True)
a = df_rates_mean['mark'][0]
b = df_rates_mean['mark'][1]
c = df_rates_mean['mark'][2]
print(df_games[df_games['id'] == df_rates_mean['id'][0]]['name'].values[0], format(a, '.3f'))
print(df_games[df_games['id'] == df_rates_mean['id'][1]]['name'].values[0], format(b, '.3f'))
print(df_games[df_games['id'] == df_rates_mean['id'][2]]['name'].values[0], format(c, '.3f'))

df_high_rates_index = df_rates_mean[df_rates_mean['mark'] > 8]
df_high_rates_games = df_games[df_games.id.isin(df_high_rates_index.id) == True].assign(score=lambda x: 1)
df_high_rates_games = df_high_rates_games.groupby('company', as_index=False).sum(numeric_only=True)
df_high_rates_games.sort_values(by='score', ascending=False, inplace=True, ignore_index=True)
print(df_high_rates_games.company[0], df_high_rates_games.score[0])

"""
games001.csv
rates001.csv
"""
