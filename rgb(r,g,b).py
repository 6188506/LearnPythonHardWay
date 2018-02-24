def rgb(r):
    r_hex = ''
    if r <= 0 or r == '':
        r_hex = '00'
    elif r > 255:
        r_hex = 'FF'
    else:
        if len(hex(r)[2:]) == 1:
            r_hex = '0' + upper(hex(r)[2:])
    return r_hex