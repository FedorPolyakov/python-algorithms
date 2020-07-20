# Определить, какое число в массиве встречается чаще всего.
import random
SIZE = 100000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
MAX = 0
MAX_KEY = -1

print(array)
d_f = {}
for char in array:
    if char in d_f:
        d_f[char] = d_f[char] + 1
    else:
        d_f[char] = 1
print(d_f)

for key, value in d_f.items():
    if value > MAX:
        MAX = value
        MAX_KEY = key

print(f'Чаще всего встречается число: {MAX_KEY}')
