def sort_list(array):
    # метод меняет местами минимальные и максимальные элементы,
    # добавляет в конец массива минимальное значение
    if len(array) == 0:
        return array
    max_num = max(array)
    min_num = min(array)
    for i in range(len(array)):
        if array[i] == max_num:
            array[i] = min_num
        elif array[i] == min_num:
            array[i] = max_num
    array.append(min_num)
    return array

print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]