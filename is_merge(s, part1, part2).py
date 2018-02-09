def is_merge(s, part1, part2):
    part1_index = [s.index(i) for i in  part1  if i in s]
    part2_index = [s.index(i) for i in  part2  if i in s]
    if part1_index == sorted(part1_index) and part2_index == sorted(part2_index) and len(s)==len(part1_index)+len(part2_index):
        return True
    else:
        return False