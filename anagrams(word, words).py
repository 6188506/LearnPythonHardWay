def anagrams(word, words):
    result = []
    word_letter_sort = sorted(word)
    for element in words:
        if len(element) == len(word):
            counter = 0
            for i in range(len(word_letter_sort)):
                if sorted(element)[i] == word_letter_sort[i]:
                    counter += 1
                    if counter == len(word):
                        result.append(element)
                else: 
                    break
    return result
	
	
####最佳解1
def anagrams(word, words): 
return [item for item in words if sorted(item)==sorted(word)]	
####最佳解2
def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)