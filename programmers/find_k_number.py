def solution(n, k):
    
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    rev_base = rev_base[::-1] 
    
    num = list( rev_base.split('0'))
    new_num = []
    for i in range(len(num)):
        if(num[i] != ''):
            new_num.append(int(num[i]))  
    answer = 0
    for i in range(len(new_num)):
        check = True
        
        if new_num[i] == 1:
            check = False
        
        elif new_num[i] == 2:
            check = True
        
        else:
            for j in range(2,new_num[i]):
                if( ((new_num[i] % j) == 0)  ):
                    check = False
                    break
                if(j * j >= new_num[i]):
                    break
                
        if(check==True):
            answer += 1
            
    
    
    return answer