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