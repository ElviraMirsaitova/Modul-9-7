    #1-й способ
def is_prime(func):
    def wrapper(*nums):
        new = func(*nums)

        for i in range(2, round(new ** 0.5)):
            if new % i  == 0:
                print('Cоставное', new)
                break

        else:
            print('Простое', new)
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result

sum_three(2, 3, 12)

    # 2-й способ
#
# def is_prime(func):
#     def wrapper(*nums):
#         new = func(*nums)
#         for i in range(new - 1):
#             if new % (i + 2) == 0:
#                 return'Cоставное'
#
#             else:
#                 return'Cоставное'
#
#     return wrapper
#
# def sum_three(a, b, c):
#     result = a + b + c
#     return result
#
# sum_three_dec = is_prime(sum_three)
#
# print(sum_three_dec(2,3,6))
# print(sum_three(2,3,6))

