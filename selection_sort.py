def selectionsort(list):
    for i in range(0,len(list)-1):
        minimum = i
       
        for j in range(i+1,len(list)):
            if list[j] < list[minimum]:
               minimum = j
            
        if minimum != i:
            
            list[minimum],list[i]= list[i],list[minimum]
            
    return list
    
print(selectionsort([7,8,2,5,3,1,4,6]))
    
