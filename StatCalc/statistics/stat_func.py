import math

def calc(lst):

    map(float,lst)
    lst.sort()
    
    output = [] ## 0:count 1: High 2:Low 3:Mean 4:Median 5:Mode 6: Mode freq. 7:SD 8:Var
    
    output.append(len(lst))
    output.append(max(lst))
    output.append(min(lst))
    output.append(sum(lst)/float(len(lst)))
    
    if len(lst)%2 != 0:
        output.append(lst[(len(lst)/2)])
    else:
         output.append((lst[len(lst)/2] + lst[(len(lst)/2)-1])/2)
    
    idx = 0
    cnt = 1
    mx = 1
    
    for i in range(1,len(lst)):
        if lst[i]==lst[i-1]:
            cnt = cnt+1
            if cnt > mx:
                mx = cnt
                idx = i
        else:
            cnt = 1
    
    output.append(lst[idx])
    output.append(cnt)
    
    var=0
    mean = sum(lst)/len(lst)
    for t in range(0,len(lst)):
        var = var + (mean-lst[t])*(mean-lst[t])
    
    var = var/len(lst)
    sd = math.sqrt(var)
    
    output.append(var)
    output.append(sd)
    
    return output