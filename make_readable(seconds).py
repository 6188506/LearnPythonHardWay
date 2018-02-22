def make_readable(seconds):
    if seconds == None:
        return "00:00:00"
    elif 0<=seconds<=59 :
        return "00:00:%02d"%seconds
    elif 60<=seconds<=3599:
        return "00:%02d:%02d"%(divmod(seconds, 60))
    else :
        return "%02d:%02d:%02d"%(seconds//3600,(seconds%3600)//60,(seconds%3600)%60)