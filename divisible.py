"""def divisible_by_7():
    result = []
    for number in range(2000 , 3200):
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    return result





print(divisible_by_7())"""

def divisible_by_seven():
    result = []
    for number in range(2000 , 3200):
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    return result


print(divisible_by_seven())