def get_factors(n):
    factor_list = []
    for i in range(2, n):
        if n % i == 0:
            factor_list.append(i)
    print(factor_list)


get_factors(6)
get_factors(12)
get_factors(20)
get_factors(7)
get_factors(1)