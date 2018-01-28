def rot13(message):
    intab =  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    outtab = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    return message.translate(message.maketrans(intab,outtab))
	
查询下 codecs.encode（'rot13'） 是啥	

def rot13(message):
    import codecs
    return codecs.encode(message, 'rot_13') 查询