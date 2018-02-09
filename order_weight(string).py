def order_weight(string):
    str_spl = string.split()
    digit_sum = [sum(map(int, list(i)))for i in str_spl]
    bind_sort = sorted(zip(digit_sum, str_spl))
    return ' '.join(zip(*bind_sort)[1])
