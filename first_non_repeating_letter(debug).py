def first_non_repeating_letter(stringX):
    import string
    for i in stringX:
        if  65 <= ord(i) <= 90 and  stringX.count(i) == 1 and stringX.count(i.lower()) == 0:
            return i
        elif  97 <= ord(i) <= 122 and  stringX.count(i) == 1 and stringX.count(i.upper()) == 0:
            return i
        elif stringX.count(i) == 1 and i in string.punctuation:    
            return i