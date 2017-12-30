def pig_it(text):
    import string
    text_splited = text.split()
    for i in range(len(text_splited)):
        if text_splited[i] in  string.punctuation:
            text_splited[i] = text_splited[i]
            #result_text = ' '.join(text_splited[i])
        else:
            text_splited[i] = text_splited[i][1:] + text_splited[i][0] + 'ay'
            #result_text = ' '.join(text_splited[i])
    return  ' '.join(text_splited)                    
    
#best practices	
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])	