def tower_builder(n):
    tower = []
    for i in range(1, n*2,2):
        tower.append(' '*(((n*2-1)-i)/2)+i*'*'+' '*(((n*2-1)-i)/2))
    print '['
    for i in tower:
        print "  " + "\'%s\'" %i + ','
    print ']'    
        
        
    #=>我觉得对的，系统没过去 ，idle中可以正常输出   