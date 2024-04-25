def multiply_numbers(inputs=""):
    # метод для нахождения произведения чисел в строке
    nums = [int(num) for num in str(inputs) if num.isnumeric()]
    if len(nums) != 0:
        S = 1
        for num in nums:
            S *= num
        return S
    return None

print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120

