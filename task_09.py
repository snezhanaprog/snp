def connect_dicts(dict1, dict2):
    # метод соединяет 2 словаря в один по правилам:
    # 1.приоритетны ключи того словаря, сумма значений ключей которого больше,
    # 2.ключи со значениями меньше 10 игнорируются,
    # 3.полученный словарь упорядочен по значениям ключей в порядке возрастания.
    sum_dict1 = sum(dict1.values())
    sum_dict2 = sum(dict2.values())
    result_dict = {}
    for key, value in dict1.items():
        if value >= 10:
            result_dict[key] = value
    for key, value in dict2.items():
        if value >= 10:
            if key in result_dict:
                if sum_dict1 < sum_dict2:
                    result_dict[key] = value
                if sum_dict2 == sum_dict1:
                    if value > result_dict[key]:
                        result_dict[key] = value
            else:
                result_dict[key] = value
    return dict(sorted(result_dict.items(), key=lambda item: item[1]))


print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # =>{ "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # => { d: 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # =>{ "c": 11, "b": 12, "a": 15 }