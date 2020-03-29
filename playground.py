# def square_digits(num):
#     result_list = []
#
#     num_as_string = str(num)
#     for i in num_as_string:
#         result = int(i) * int(i)
#         print(result)
#
#         result_list.append(str(result))
#
#     result_string = "".join(result_list)
#     return result_string

# ________________________________________________
# def solution(string):
#     # letters = string.split(' ')
#     list = []
#     for letter in string:
#         list.append(letter)
#
#     list.reverse()
#     list_string = "".join(list)
#     return list_string
#
# result = solution('labas')
# print(result)

# _________________________________________________
# def odd_or_even(arr):
#     result = 0
#     for number in arr:
#         result = number + result
#     if result % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'

# a = odd_or_even([1, 2])
# print(a)

# _________________________________________________
# def square_sum(numbers):
#     sum = 0
#     for number in numbers:
#         square_number = number**2
#         sum = square_number + sum
#     return sum
#
# a = square_sum([1, 2, 2])
# print(a)

# _________________________________________________
# def invert(lst):
#     new_list = [-x for x in lst]
#     return new_list
#     new_list = []
#     for item in lst:
#         new_list.append(-item)
#     return new_list
#
# a = invert([-1, 2, -4, 9])
# print(a)

# _________________________________________________
# def remove_char(s):
#     list = []
#     for letter in s:
#         list.append(letter)
#         print(list)
#         list.pop(0)
#         return list
#
# a = remove_char('labas')
# print(a)

# _________________________________________________
# def basic_op(operator, value1, value2):
#     if operator == '+':
#         result = value1 + value2
#     elif operator == '-':
#         result = value1 - value2
#     elif operator == '*':
#         result = value1 * value2
#     elif operator == '/':
#         result = value1 / value2
#     return result

# a = basic_op("-", 2, 5)
# print(a)

# _________________________________________________
def make_upper_case(s):
    return s.upper()

a = make_upper_case('labas')
print(a)