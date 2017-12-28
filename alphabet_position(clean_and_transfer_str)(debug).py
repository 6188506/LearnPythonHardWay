def alphabet_position(text):
    import string
    alph_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    output = []
    text_cleaned = ''
    #clean
    for i in text:
        if i in string.punctuation or i==' ':
            pass
        else:
            text_cleaned = text_cleaned + i
    #calcuate
    for i in text_cleaned:
       output.append(alph_dict[i.lower()])
    return ' '.join(map(str, output))    