def strip_url_params(url, params_to_strip = []):
    find_rep_element = ''
    url_split_by_QMark = url.split('?')
    if url.split('?') == None:
        return url
    else:
        split_by_and = sorted(url_split_by_QMark[1].split['&'])
            for i in split_by_and[0]： #=>开始提前重复的元素 ,但是只做了其中一个，显然应该便利所以元素       
                if i == '=':
                    break
                else:
                    find_rep_element = ''.join(i)
                    