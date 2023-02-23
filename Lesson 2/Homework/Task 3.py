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
import numpy as np

