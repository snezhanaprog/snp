def isfloat(value):
    # метод, который проверяет является ли параметр типом float
    try:
        float(value)
        return True
    except:
        return False

def max_odd(array):
    # метод, определяющий максимальных нечётный элемент в массиве
    max_num = None
    for item in array:
        if isfloat(item) and item % 2 != 0:
            if max_num is None or item > max_num:
                max_num = item
    return max_num


print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4])) # => None