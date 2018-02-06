def valid_parentheses(string):
    left_par_counter = 0
    right_par_counter = 0
    if len(filter(lambda x:x=='(', list(string)))==len(filter(lambda x:x==')', list(string))):
        for i in string:
            if i == '(':
                left_par_counter += 1
            if i == ')':
                right_par_counter += 1
            if cmp(left_par_counter, right_par_counter) == -1 :
                return False              
        return True
    else:
        return False
		
		
####最佳实践

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False		
		