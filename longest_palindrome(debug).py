def longest_palindrome (s):
    result = []
    for i in range(len(s)):
        e = i + 1
        while e <= len(s):
            if s[i:e] == s[i:e][::-1]:
                result.append(len(s[i:e]))
            e += 1
    return max(result)        
            