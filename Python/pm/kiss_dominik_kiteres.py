def kiteres(x:list, k:int):
    elott = []
    utan = []
    
    for i in range(len(x)):
        if i < k:
            elott.append(x[i])
        elif i > k:
            utan.append(x[i])
        
    min = elott[0]
    max = utan[0]
    
    for i in range(1, len(elott)):
        if min > elott[i]:
            min = elott[i]
            
    for i in range(1, len(utan)):
        if max < utan[i]:
            max = utan[i]
            
    elteres = abs(min - max)
    return elteres