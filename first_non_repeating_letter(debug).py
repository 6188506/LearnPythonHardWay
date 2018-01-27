def first_non_repeating_letter(string):
    dict = {}
    counter = 0
    for index, value in enumerate(string):
        dict[index] = value
    for i in string.lower():
        counter += 1
        if string.lower().count(i)==1:
            return dict[counter-1]