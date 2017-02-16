import lab04

print(lab04.reverse_iter([1, 2, 3, 4]))

print(lab04.reverse_recursive([1, 2, 3, 4]))

print(lab04.map(lambda x: x*x, [1, 2, 3]))

print(lab04.filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

print(lab04.reduce(lambda x, y: x + y, [1, 2, 3, 4]))
