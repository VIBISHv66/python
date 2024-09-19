def mergesort(array):

    if len(array) >1 :
        middle=len(array)//2
        left=array[: middle]
        right=array[middle:]
        mergesort(left) 
        mergesort(right)
        lp = 0
        rp = 0
        fp = 0
        while (lp<len(left) and rp<len(right)):
            if left[lp]<right[rp]:
                array[fp]=left[lp]
                lp+=1
            else:
              array[fp]=right[rp]
              rp+=1
              fp+=1
        while(lp<len(left)):
             array[fp]=left[lp]
             fp+=1
             lp+=1
        while(rp<len(right)):
             array[fp]=right[rp]
             fp += 1
             rp += 1
    return array
array= [3,6,1,5,9,7,2]
print(array)
sort_array = mergesort(array)
print(sort_array)




