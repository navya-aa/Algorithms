def quicksort(elements):
    n=len(elements)
    if(n<=1):
        return elements
    else:
        p= elements.pop()
    right=[]
    left=[]
    
    for i in elements:
        if i>p:
            right.append(i)
        else:
            left.append(i)
    return quicksort(left)+[p]+quicksort(right)
print (quicksort([6,4,8,3,1,2,5,7,9]))
        
