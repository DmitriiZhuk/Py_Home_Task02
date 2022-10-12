# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

template = "one"
initial_string = "onetwonine"

for i in template:
    x = initial_string.count(i)
    print(f"{i} встречается в строке {initial_string} {x} раз")
