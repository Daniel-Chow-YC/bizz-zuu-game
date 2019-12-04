def div_by_3(num):
    return num % 3 == 0

def div_by_5(num):
    return num % 5 == 0

def div_by_3_and_5(num):
    return div_by_5(num) and div_by_3(num)
