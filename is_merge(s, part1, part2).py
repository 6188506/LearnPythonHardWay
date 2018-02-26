def is_merge(s, part1, part2):
    s_list = list(s)
    part1_index = [s.index(i) for i in part1  if i in s]
    
    if part1_index == sorted(part1_index) and len(part1+part2)==len(s):
        for i in part1:
            s_list.remove(i)
        result = ''.join(s_list)
        if result == part2:
            return True
        else:
            return False
    else: 
        return False