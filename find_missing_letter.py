def find_missing_letter(chars):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    compare_chars = alphabet[alphabet.index(chars[0]):alphabet.index(chars[0])+len(chars)]
    for n in range(len(chars)):
        if compare_chars[n] != chars[n]:
           break
    return compare_chars[n]                  
