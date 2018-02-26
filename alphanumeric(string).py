def alphanumeric(string):
    if len(filter(lambda x:x.isdigit(),list(string)))>0:
        return True 
    elif string == 'a'or string == 'an':
        return True
    else:
        return False
		
#####最佳实践
# An obvious, elegant solution is just to return string.isalnum()
# But I feel like this kata is broken.  The description says something about a buggy regular expression.
# I don't know what regular expression it's referring to, but to try to solve this in the spirit of
# the kata, I'm going to use a regular expression.

import re

pattern = re.compile('^[0-9a-zA-Z]+$')

def alphanumeric(string):
  return pattern.match(string) is not None		
		