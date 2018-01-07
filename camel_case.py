def to_camel_case(text):
    import re
    
    return re.split('-|_',text)[0]+''.join([value.capitalize() for index,value in enumerate(re.split('-|_',text)) if index != 0])
	
##########################################################
best pracitce
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s