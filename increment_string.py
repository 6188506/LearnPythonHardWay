def increment_string(strng):
    import re
    pattern = r'([a-zA-Z]*)(\d*)'
    match = re.search(pattern, strng)
    length = len(match.group(2))
    if strng == '': 
        return 1
    elif match.group(2) == '':
        return strng+'1'
    else: 
        return '%0\length'%(int(match.group(2)) + 1)