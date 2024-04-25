import datetime
def date_in_future(num = None):
    # метод для возвращение даты через num дней
    if type(num) == int:
        date = datetime.datetime.now() + datetime.timedelta(days=num)
        return date.strftime('%d-%m-%Y %H:%M:%S')
    return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня