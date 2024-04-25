def isfloat(value):
    # метод, который проверяет является ли параметр типом float
    try:
        float(value)
        return True
    except:
        return False

def coincidence(list_params="", mas_range=""):
    # метод для определения элементов из массива list, входящих в диапазон range
    result = []
    for item in list_params:
        if isfloat(item) and mas_range[0] <= float(item) <= mas_range[-1]:
            result.append(item)
    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
print(coincidence()) # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]