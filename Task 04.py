# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

# сначала делаю 
# pip install numpy

# Collecting numpy
#   Downloading numpy-1.23.4-cp310-cp310-win_amd64.whl (14.6 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.6/14.6 MB 12.6 MB/s eta 0:00:00
import numpy as np

num = int(input("Введите N элементов: "))
move_forward = 2

initial_array = list(range(-num, num+1))
print(initial_array)

final_array = np.roll(initial_array, move_forward)
print(final_array)
